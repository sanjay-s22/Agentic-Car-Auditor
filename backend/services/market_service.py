import re
import requests
from ddgs import DDGS
from statistics import median, mean

def fetch_with_jina(url: str) -> str:
    try:
        response = requests.get(f'https://r.jina.ai/{url}', timeout=10)
        if response.status_code == 200:
            return response.text
    except requests.RequestException as e:
        print(f'JINA ERROR: {e}')
    return ''

_PRICE_PATTERN = re.compile(
    r'(?:₹|rs\.?|inr)\s*([\d,]+(?:\.\d+)?)\s*(lakh|lac|crore|cr|l)?\b',
    re.IGNORECASE,)

_YEAR_PATTERN = re.compile(r'\b(19[5-9]\d|20[0-4]\d)\b')
_KM_PATTERN = re.compile(r'([\d,]+)\s*k?ms?\b', re.IGNORECASE)
_UNIT_MULTIPLIER = {
    'lakh': 100_000, 'lac': 100_000, 'l': 100_000,
    'crore': 10_000_000, 'cr': 10_000_000,
}

def extract_listings(text: str, window: int = 200):
    listings = []
    for match in _PRICE_PATTERN.finditer(text):
        num_str, unit = match.groups()
        try:
            value = float(num_str.replace(',', ''))
        except ValueError:
            continue

        unit = (unit or '').lower()
        if unit in _UNIT_MULTIPLIER:
            value *= _UNIT_MULTIPLIER[unit]
        elif value < 1000:
            continue

        start, end = match.span()
        context = text[max(0, start - window): end + window]
        year_match = _YEAR_PATTERN.search(context)
        km_match = _KM_PATTERN.search(context)

        listings.append({
            'price': int(value),
            'year': int(year_match.group(1)) if year_match else None,
            'km': int(km_match.group(1).replace(',', '')) if km_match else None,
        })

    return listings

def get_market_data(
    brand,
    model,
    city,
    year=None,
    fuel_type=None,
    km_driven=None,
    owner=None,
    trusted_domains=('cars24', 'cardekho', 'spinny', 'carwale', 'cartrade'),
    excluded_terms=(),
    min_price=100_000,
    max_price=20_000_000,
):
    query = f'{brand} {model} used car {city}'

    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=20))

    print('\nQUERY:', query)
    print('COUNT:', len(results))

    filtered_results = []
    for result in results:
        href = result.get('href', '').lower()
        if model.lower() not in href:
            continue

        text = (result.get('title', '') + ' ' + result.get('body', '')).lower()

        domain_match = any(domain in href for domain in trusted_domains)
        brand_match = brand.lower() in text
        model_match = model.lower() in text
        excluded_match = any(term.lower() in text for term in excluded_terms)

        if domain_match and brand_match and model_match and not excluded_match:
            filtered_results.append(result)

    print('\nFILTERED RESULTS:', len(filtered_results))

    all_listings = []
    for result in filtered_results:
        url = result.get('href', '')
        text = fetch_with_jina(url)
        if not text:
            text = result.get('title', '') + ' ' + result.get('body', '')

        listings = [
            l for l in extract_listings(text)
            if min_price <= l['price'] <= max_price
        ]
        if listings:
            print('\nFOUND LISTINGS')
            print(url)
            print(listings[:10])
            all_listings.extend(listings)

    seen = set()
    unique_listings = []
    for l in all_listings:
        key = (l['price'], l['year'], l['km'])
        if key not in seen:
            seen.add(key)
            unique_listings.append(l)

    print('\nALL LISTINGS:', unique_listings)

    confidence = 'low'
    if year:
        tier1 = [l['price'] for l in unique_listings
                 if l['year'] is not None and abs(l['year'] - year) <= 2]
        tier2 = [l['price'] for l in unique_listings
                 if l['year'] is not None and abs(l['year'] - year) <= 5]

        if len(tier1) >= 3:
            prices, confidence = tier1, 'high'
        elif len(tier2) >= 3:
            prices, confidence = tier2, 'medium'
        else:
            prices = [l['price'] for l in unique_listings]
    else:
        prices = [l['price'] for l in unique_listings]

    if prices:
        median_price = round(median(prices))
        average_price = round(mean(prices))
        lowest_price = min(prices)
        highest_price = max(prices)
    else:
        median_price = average_price = lowest_price = highest_price = None

    market_data = {
        'avg_market_price': median_price,
        'average_price': average_price,
        'lowest_price': lowest_price,
        'highest_price': highest_price,
        'listing_count': len(filtered_results),
        'price_sample_size': len(prices),
        'confidence': confidence if year else 'unscored',
        'sources': filtered_results,
    }

    print('\nMARKET DATA')
    print(market_data)
    return market_data