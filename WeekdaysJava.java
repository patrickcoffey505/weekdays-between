

public class WeekdaysJava {
  public static void main(String[] args) {
    System.out.println(Weekdays(1, 1, 1, 12));
  }

  public static int Weekdays(int first_month, int first_day, int second_month, int second_day)
  {
    int[] month_list = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
    int[] WEEKEND = { 2, 3 };

    int first_date = 0;
    int second_date = 0;
    int num_weekdays = 0;

    //get num days for date 1 since epoch
    for (int i = 0; i < first_month - 1; i++)
      first_date += month_list[i];
    first_date += first_day;

    //get num days for date 2 since epoch
    for (int i = 0; i < second_month - 1; i++)
      second_date += month_list[i];
    second_date += second_day;

    //get num days between date 1 and date 2
    int days_between = second_date - first_date;

    //for each full week between, add 5 to num_weekdays
    while (days_between >= 7) {
      num_weekdays += 5;
      days_between -= 7;
    }

    //for remaining days, determine what days are weekdays and add them to num_weekdays
    while (days_between > 0) {
      if (first_date % 7 != WEEKEND[0] && first_date % 7 != WEEKEND[1])
         num_weekdays += 1;
      days_between--;
      first_date++;
    }

    return num_weekdays;
  }
}
