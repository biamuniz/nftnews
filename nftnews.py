def nftnews():
    from GoogleNews import GoogleNews
    import pandas as pd
    googlenews=GoogleNews(period='d')
    googlenews.setlang('pt')
    googlenews.search('NFT')
    result=googlenews.result()
    df=pd.DataFrame(result)
    del df['datetime']
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    return df
