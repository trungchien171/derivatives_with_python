from GBM_returns import *

# Read data for the EURIBOR
def read_euribor_data():
    ''' Read historical Euribor data from Excel file, calculate
    log returns, realized variance and volatility'''
    EBO = pd.read_excel('./03_market_stylized_facts/EURIBOR_current.xlsx', index_col=0, parse_dates=True)
    EBO['returns'] = np.log(EBO['1w'] / EBO['1w'].shift(1))
    EBO = EBO.dropna()
    return EBO

# Plot the Term structure
markers = [',', '-.', '--', '-']

def plot_term_structure(data):
    ''' Plot the term structure of the Euribor rates '''
    plt.figure(figsize=(10, 5))
    for i, mat in enumerate(['1w', '1m', '6m', '12m']):
        plt.plot(data[mat].index, data[mat].values, 'b%s' % markers[i], label=mat)

    plt.grid(True)
    plt.legend()
    plt.xlabel('strike')
    plt.ylabel('implied volatility')
    plt.ylim(0.0, plt.ylim()[1])

if __name__ == '__main__':
    EBO = read_euribor_data()
    plot_term_structure(EBO)
    plt.show()
