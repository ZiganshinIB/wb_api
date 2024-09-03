from .baseAPI import BaseAPI
from .http_methods import HttpMethod

class SupplyAPI(BaseAPI):
    def __init__(self, parent):
        super().__init__(
            parent,
            base_url="https://supplies-api.wildberries.ru")


    def acceptance_coefficients(self, warehouse_ids: list = None):
        """
        Коэффициенты приёмки
        :param warehouse_ids: ID складов. По умолчанию возвращаются данные по всем складам
        :return: list
        [
            {
                "date": str Дата начала действия коэффициента,
                "coefficient": int Коэффициент приёмки: -1 - Поставка не доступна, 0 - бесплатная поставка, >1 -  множитель стоимости приёмки,
                "warehouseId": int ID склада,
                "warehouseName": str Название склада,
                "boxTypeName": str Тип поставки::
                    * "Короба"
                    * "Монопаллеты"
                    * "Суперсейф"
                    * "QR-поставка с коробами"
                "boxTypeID": int ID типа поставки::
                    * 2 - Короба
                    * 5 - Монопаллеты
                    * 6 - Суперсейф
                    !Для типа поставки QR-поставка с коробами поле не возвращается!
            },
            ...
        ]
        """
        url = '/api/v1/acceptance/coefficients'
        if warehouse_ids is None:
            return self (
                method_name=HttpMethod.GET,
                url=url,
            )
        return self (
            method_name=HttpMethod.GET,
            url=url,
            params={'warehouseIds': ','.join(map(str, warehouse_ids))})


    def acceptance_options(self, quantity: int, barcode: str):
        """
        Опции приёмки
        :param quantity: Количество
        :param barcode: Штрих-код
        :return: json
        {
            "result" : [
                {
                    "barcode": str Баркод из карточки товара,
                    "error":  Данные ошибки при наличии
                    {
                        "title": str ID ошибки,
                        "detail": str Описание ошибки
                    },
                    "isError": bool  True Наличие ошибки. Поля отсутствуют в случае отсутствия ошибки,
                    "warehouses": list Список складов. При наличии ошибки будет null
                    [
                        {
                            "warehouseId": int ID склада,
                            "canBox": bool True - Короба доступна, False - Короба недоступна
                            "canMonopallet": bool True - Монопаллеты доступны, False - Монопаллеты недоступны
                            "canSuperbox": bool True - Суперсейф доступен, False - Суперсейф недоступен
                        },
                        ...
                    ]
                }
            ]
        }
        """
        url = '/api/v1/acceptance/options'
        return self (
            method_name=HttpMethod.POST,
            url=url,
            data={'quantity': quantity, 'barcode': barcode})

    def warehouses(self):
        """
        Список складов
        :return: list
        [
            {
                "warehouseId": int ID склада,
                "name": str Название склада,
                "address": str Адрес склада,
                "workTime": str Время работы склада,
                "acceptsQr": bool True - QR-поставка доступна, False - QR-поставка недоступна
            },
            ...
        ]
        """
        url = '/api/v1/warehouses'
        return self (
            method_name=HttpMethod.GET,
            url=url)






