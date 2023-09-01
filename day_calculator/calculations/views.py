from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import timedelta, date


class DateCalculationView(APIView):
    """This class used for day calculation"""

    def post(self, request, format=None):
        """Used to day calculation without include fridays"""

        first_date = request.data.get("first_date")
        last_date = request.data.get("last_date")

        if first_date and last_date:
            first_year, first_month, first_day = map(int, first_date.split("-"))
            last_year, last_month, last_day = map(int, last_date.split("-"))
            first_date = date(first_year, first_month, first_day)
            last_date = date(last_year, last_month, last_day)
            total_days = (last_date - first_date).days + 1
            fridays = sum(
                1
                for d in range(total_days)
                if (first_date + timedelta(days=d)).weekday() == 4
            )
            day_without_friday = total_days - fridays

            return Response({"total_days": day_without_friday})

        return Response("Double check please")
