import polygon

import pandas as pd
import numpy as np
from local_settings import polygonAPIkey as settings




if __name__ == '__main__':
    reference_client = polygon.ReferenceClient(settings['APIkey'])
    df = pd.DataFrame(reference_client.get_tickers(market='stocks'))

    cols = ['ticker', 'name', 'market', 'locale', 'primary_exchange', 'type', 'active', 'currency_name', 'cik',
            'composite_figi', 'share_class_figi', 'last_updated_utc']

    results = pd.DataFrame(columns=cols)
    results['active'] = results['active'].astype(bool)

    for row in df.itertuples():
        single_result = pd.DataFrame(data=row.results, index = [0])
        single_result['active'].astype('bool')
        results = pd.concat([results, single_result])


    print(results)