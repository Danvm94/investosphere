from models import Portfolio


def get_or_create_portfolio(user, portfolio_name):
    try:
        portfolio = Portfolio.objects.get(user=user, name=portfolio_name)
    except Portfolio.DoesNotExist:
        portfolio = Portfolio.objects.create(user=user, name=portfolio_name)
    return portfolio
