month=input("ENTER MONTH")
match month:
    case m if m in( "january"," march", "may", "july", "august"," october"," december"):print("31 days")
    case m if m in ( "febuary"):print("28 or 29 days")
    case m if m in ("april", "june", "september", "november"):print("30 days")
