import numpy as np
import random
import matplotlib.pyplot as plt
import math

def assess_risk(portfolio):
    returns = np.array([random.uniform(0.05, 0.15) for _ in range(1000)])  # Simulate returns
    volatility = np.std(returns)  # Calculate standard deviation (volatility)
    avg_return = np.mean(returns)
    sharpe_ratio = avg_return / volatility

    # Plot risk vs. return
    plt.scatter(volatility, avg_return, color='blue')
    plt.title('Risk vs. Return of Portfolio')
    plt.xlabel('Volatility (Risk)')
    plt.ylabel('Average Return')
    plt.show()

    return volatility, avg_return, sharpe_ratio

# Example usage
assess_risk([0.6, 0.4])  # Portfolio with 60% stocks, 40% bonds
