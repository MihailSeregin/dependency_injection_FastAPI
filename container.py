from dependency_injector import containers, providers
from sorters import *
from value_provider import ValueProvider

class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=["endpoints"])

    config = providers.Configuration()

    value_provider = providers.Singleton(ValueProvider, quantity=config.value_provider.quantity)
    sorter_values = providers.Singleton(SorterValues, limit=config.sorters.limit)
    substractor = providers.Singleton(Substractor, substractor_digit=config.sorters.substractor_digit)

    pipeline = providers.Factory(
        Pipeline,
        value_provider=value_provider,
        sorter_values=sorter_values,
        substractor=substractor)

    

 