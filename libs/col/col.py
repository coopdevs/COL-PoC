import uno

from com.sun.star.beans import PropertyValue
from com.sun.star.text import XSimpleText

from . import constants

class Col:
    def __init__(self, hostname, port, filename):
        self._crop_idx = 0

        local_context = uno.getComponentContext()
        resolver = local_context.ServiceManager.createInstanceWithContext(
            "com.sun.star.bridge.UnoUrlResolver", local_context
        )
        connectionString = "socket,host=%s,port=%s;urp;StarOffice.ComponentContext" % (hostname, port)
        context = resolver.resolve("uno:%s" % connectionString)
        desktop = context.ServiceManager.createInstanceWithContext(
            "com.sun.star.frame.Desktop", context
        )
        hidden = PropertyValue("Hidden", 0, True, 0)
        self._doc = desktop.loadComponentFromURL(filename, "_blank", 0, (hidden,))
        self._sheets = self._doc.getSheets()

    def add_crops(self, crop_type, surface, selling_price, production):
        # TODO: Validate decimal values
        if crop_type not in constants.CROPS.keys():
            raise Exception()

        if self._crop_idx >= constants.MAX_CROPS:
            raise Exception()

        crop_description = constants.CROPS[crop_type]
        ranges = constants.INPUT_CELLS[self._crop_idx]

        # increase crop idx for subsequent calls
        self._crop_idx += 1

        input_sheet = self._sheets.getByName(constants.INPUT_SHEET)
        input_data = [crop_description, surface, selling_price, production]

        for idx, cell_range in enumerate(ranges):
            cell = input_sheet.getCellRangeByName(cell_range)
            cell.insertString(cell.Text.createTextCursor(), input_data[idx], True)

        self._doc.calculateAll()

    def set_working_costs(self, qualified, non_qualified):
        # TODO: Validate decimal values
        input_sheet = self._sheets.getByName(constants.INPUT_SHEET)

        cell = input_sheet.getCellRangeByName(constants.QUALIFIED_COST_CELL)
        cell.insertString(cell.Text.createTextCursor(), qualified, True)

        cell = input_sheet.getCellRangeByName(constants.NON_QUALIFIED_COST_CELL)
        cell.insertString(cell.Text.createTextCursor(), non_qualified, True)

        self._doc.calculateAll()

    def get_results_table(self, crop_type, result_type):
        if crop_type not in constants.CROPS.keys():
            raise Exception()

        if result_type not in constants.RESULT_TYPES.keys():
            raise Exception()


        crop_description = constants.CROPS[crop_type]
        result_description = constants.RESULT_TYPES[result_type]

        results_sheet = self._sheets.getByName(constants.RESULTS_SHEET)

        cell = results_sheet.getCellRangeByName(constants.RESULT_CROP_CELL)
        cell.insertString(cell.Text.createTextCursor(), crop_description, True)

        cell = results_sheet.getCellRangeByName(constants.RESULT_TYPE_CELL)
        cell.insertString(cell.Text.createTextCursor(), result_description, True)

        self._doc.calculateAll()
        
        tables_sheet = self._sheets.getByName(constants.TABLES_SHEET)
        result_table = tables_sheet.getCellRangeByName(constants.RESULT_TABLE_RANGE)

        # TODO: make this data pretty
        return result_table.getDataArray()

    def get_results_chart(self, crop_type, result_type):
        if crop_type not in constants.CHART_SHEETS.keys():
            raise Exception()

        if result_type not in constants.CHARTS.keys():
            raise Exception()

        crop_sheet = constants.CHART_SHEETS[crop_type]
        chart_ranges = constants.CHARTS[result_type]

        chart_sheet = self._sheets.getByName(crop_sheet)
        data = []
        for data_range in chart_ranges:
            chart_table = chart_sheet.getCellRangeByName(data_range)
            for row in chart_table.getDataArray():
                data.append(row)

        # TODO: make this data pretty
        return data
