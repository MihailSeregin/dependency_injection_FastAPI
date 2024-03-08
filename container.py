from dependency_injector import containers, providers
from sorters import *
from value_provider import ValueProvider

class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=["endpoints"])

    config = providers.Configuration()

    value_provider = providers.Singleton(ValueProvider, quantity=2)

    sorter_values = providers.Singleton(SorterValues, 5)
    substractor = providers.Singleton(Substractor, substractor_digit=2)

    pipeline = providers.Factory(
        Pipeline,
        value_provider=value_provider,
        sorter_values=sorter_values,
        substractor=substractor)

    

