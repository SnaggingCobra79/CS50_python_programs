def main():
    while True:

        combined = input("Enter the date in mm.dd.yy: ").strip()
        try:
            combined = combined.replace(",","")
            if any(c.isalpha() for c in combined) and ("/" in combined or "." in combined):
                raise ValueError

            if "/" in combined:
                parts = combined.split("/")
            elif "." in combined:
                parts = combined.split(".")
            else:
                parts = combined.split()

            if len(parts) != 3:
                raise ValueError


            if len(parts) == 3:
                month, date, year = parts


                if month.isdigit() and date.isdigit() and year.isdigit():
                    date = int(date)
                    month = int(month)
                    if 1 <= month <= 12 and 1 <= date <= 31:
                        print(f"{year}-{month:02}-{date:02}")
                        break
                    else:
                        raise NameError

                elif month.isalpha() and date.isdigit() and year.isdigit():

                    amonth = [
                            "January", "February", "March", "April", "May", "June",
                            "July", "August", "September", "October", "November", "December"
                            ]
                    for m in amonth:
                        if m.lower() == month.lower():
                            nummonth = amonth.index(m) + 1
                            date = int(date)
                            if 1 <= date <= 31:
                                print(f"{year}-{nummonth:02}-{date:02}",end = " ").strip()
                                break

                            else:
                                raise ValueError


        except (ValueError,NameError):
            continue

main()
