from .baseAPI import BaseAPI
from .http_methods import HttpMethod

class ContentAPI(BaseAPI):
    def __init__(self, parent):
        super().__init__(parent, base_url="https://content-api.wildberries.ru")


    def cards_upload(self, subject_id: int, variants: list):
        """
        Создание карточки товара
        :param subject_id: ID предмета
        :param variants: Массив вариантов товара. В каждой КТ может быть не более 30 вариантов (НМ)
        :return:
        """
        return self (
            method_name=HttpMethod.POST,
            url='/content/v2/cards/upload',
            data={
                'subjectId': subject_id,
                'variants': variants,
            })


    def cards_update(
            self, nm_id: int, vendor_code: str,sizes: list,
            brand: str = None, title: str = None,
            description: str = None, dimensions: dict = None,
            characteristics: dict = None):
        """
        Редактирование КТ
        :param nm_id: Артикул WB
        :param vendor_code: Артикул продавца
        :param sizes: Массив размеров артикула. Для безразмерного товара все равно нужно передавать данный массив без параметров (wbSize и techSize), но с баркодом.

        :param brand: Бренд
        :param title: Наименование товара
        :param description: Описание товара. Максимальное количество символов зависит от категории товара. Стандарт — 2000, минимум — 1000, максимум — 5000.
Подробно о правилах описания в Правилах заполнения карточки товара в разделе Инструкции на портале продавцов.
        :param dimensions: Габариты упаковки товара. Указывать в сантиметрах для любого товара. {length: int, width: int, height: int}
        :param characteristics: Характеристики товара {'id' - int, 'value' - any}

        :return: json {data, error, errorText, additionalErrors}
        """
        url = '/content/v2/cards/upload/add'
        data = {
            'nmId': nm_id,
            'vendorCode': vendor_code,
            'sizes': sizes,
        }
        if brand is not None:
            data['brand'] = brand
        if title is not None:
            data['title'] = title
        if description is not None:
            data['description'] = description
        if dimensions is not None:
            data['dimensions'] = dimensions
        if characteristics is not None:
            data['characteristics'] = characteristics
        return self (
            method_name=HttpMethod.POST,
            url=url,
            data=data)

    def cards_moveNM(self, nm_ids: list[int], target_IMT: int = None):
        """
        Объединение / Разъединение НМ
        :param target_IMT: Существующий у продавца imtID, под которым необходимо объединить НМ. Если параметр не передан, то НМ будут разъединены
        :param nm_ids: которые необходимо объединить / разъединить (максимум 30)
        :return: json
        """
        url = '/content/v2/cards/moveNM'
        data = {
            'nmIds': nm_ids
        }
        if target_IMT is not None:
            data['targetIMT'] = target_IMT
        return self (
            method_name=HttpMethod.POST,
            url=url,
            data=data)

    def barcodes(self, count: int = None):
        """
        Метод позволяет сгенерировать массив уникальных баркодов для создания размера НМ в КТ.
        :param count: Кол-во баркодов которые надо сгенерировать, максимальное доступное количество баркодов для генерации - 5 000
        :return: json {data, error, errorText, additionalErrors}
        """
        url = '/content/v2/barcodes'
        if count is None:
            return self (
                method_name=HttpMethod.POST,
                url=url,
            )
        return self(
            method_name=HttpMethod.POST,
            url=url,
            data={'count': count}
        )

    def get_cards_list(self, locale: str = None, settings: dict = None):
        """
        Метод позволяет получить список созданных НМ с фильтрацией по разным параметрам, пагинацией и сортировкой.
        :param locale:
        :param settings:
        :return:
        """
        url = '/content/v2/get/cards/list'
        if locale is None:
            if settings is None:
                return self (
                    method_name=HttpMethod.POST,
                    url=url,
                )
            return self (
                method_name=HttpMethod.POST,
                url=url,
                data={'settings': settings}
            )
        if settings is None:
            return self (
                method_name=HttpMethod.POST,
                url=url,
                params={'locale': locale}
            )
        return self (
            method_name=HttpMethod.POST,
            url=url,
            params={'locale': locale},
            data={'settings': settings}
        )

    def cards_error_list(self, locale: str = None):
        """
        Метод позволяет получить список НМ с ошибками.
        :param locale:
        :return:
        """
        url = '/content/v2/cards/error/list'
        if locale is None:
            return self (
                method_name=HttpMethod.POST,
                url=url,
            )
        return self (
            method_name=HttpMethod.POST,
            url=url,
            params={'locale': locale}
        )

    def cards_limits(self):
        """
        Метод позволяет получить отдельно бесплатные и платные лимиты продавца на создание карточек товаров.
        :return:
        """
        return self (
            method_name=HttpMethod.GET,
            url='/content/v2/cards/limits'
        )
