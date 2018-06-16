MAX_CROPS = 7

CT_OPERATIONS_COSTS= "operations_costs"
CT_TRACTOR_SCHEDULE = "tractor_schedule"
CT_LABOUR_SHCEDULE = "labour_schedule"
CT_MONTHLY_BALANCE = "monthly_balance"
CT_REQUIREMENT_COSTS= "requirements_costs"
CT_OPERATIONS_UNITARY_COSTS = "operations_unitary_costs"
CT_REQUIREMENT_UNITARY_COSTS = "requirements_unitary_costs"

RESULT_TYPES= {
  CT_OPERATIONS_COSTS: "Distribució de costos entre els grups d'operacions (€ total)",
  CT_LABOUR_SHCEDULE: "Calendari de necessitats de mà d'obra",
  CT_TRACTOR_SCHEDULE: "Calendari de necessitats de tractor",
  CT_MONTHLY_BALANCE: "Balanç mensual de costos i ingressos",
  CT_REQUIREMENT_COSTS: "Distribució de costos entre els diferents requeriments del cultiu (%)",
  CT_OPERATIONS_UNITARY_COSTS: "Distribució de costos unitaris entre els grups d'operacions",
  CT_REQUIREMENT_UNITARY_COSTS: "Part del cost unitari que representa cada requeriment",
}

CU_COL = "col"
CU_BROCOLI = "brocoli"
CU_CALCOT = "calcot"
CU_ENCIAM = "enciam"
CU_BLEDES = "bledes"
CU_TOMAQUET = "tomaquet"
CU_CARBASSA = "carbassa"

CROPS = {
  CU_COL: "Col",
  CU_BROCOLI: "Bròcoli",
  CU_CALCOT: "Calçot",
  CU_ENCIAM: "Enciam",
  CU_BLEDES: "Bledes",
  CU_TOMAQUET: "Tomàquet",
  CU_CARBASSA: "Carbassa",
  "global": "global",
}

# Chart location
CHARTS = {
    CT_OPERATIONS_COSTS: ["C519", "C521:D528"],
    CT_TRACTOR_SCHEDULE: ["E548:P548", "E585:P585"],
    CT_LABOUR_SHCEDULE: ["E594:P594", "E631:P631"],
    CT_MONTHLY_BALANCE: ["E520:P520", "E533:P533"],
    CT_REQUIREMENT_COSTS: ["D898", "F900:L901", "O900:P901"],
    CT_OPERATIONS_UNITARY_COSTS: ["C534", "C521:C528", "D536:D543", ],
    CT_REQUIREMENT_UNITARY_COSTS: ["D902", "F900:L900", "O900:P900", "F902:L902", "O902:P902"],
}

# Sheets
INPUT_SHEET = "Entrada"
RESULTS_SHEET = "Resultats"
TABLES_SHEET = "Taules"

CHART_SHEETS = {
    CU_COL: "Cu1",
    CU_BROCOLI: "Cu2",
    CU_CALCOT: "Cu3",
    CU_ENCIAM: "Cu4",
    CU_BLEDES: "Cu5",
    CU_TOMAQUET: "Cu6",
    CU_CARBASSA: "Cu7",
    "global": "global",
}


# Cells

# Crop type, surface, price, production
INPUT_CELLS = [
    ("C3", "E3", "I3", "L3", ),
    ("C6", "E6", "I6", "L6", ),
    ("C9", "E9", "I9", "L9", ),
    ("C12", "E12", "I12", "L12", ),
    ("C15", "E15", "I15", "L15", ),
    ("C18", "E18", "I18", "L18", ),
    ("C21", "E21", "I21", "L21", ),
]

QUALIFIED_COST_CELL = "O5"
NON_QUALIFIED_COST_CELL = "Q5"

RESULT_CROP_CELL = "D4"
RESULT_TYPE_CELL = "D10"

RESULT_TABLE_RANGE = "B3:O30"
