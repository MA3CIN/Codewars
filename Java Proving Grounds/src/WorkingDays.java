import java.time.LocalDate;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.Stream;
import java.time.DayOfWeek;

public class WorkingDays {

	public static void main(String[] args) {
		LocalDate startDate = LocalDate.of(2012, 3, 7);
		LocalDate endDate = LocalDate.of(2012, 6, 7);
		
		final Set<DayOfWeek> businessDays = Set.of(
			    MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY
			);

		List<LocalDate> allDates =
		startDate.datesUntil(endDate)
	        .filter(t -> businessDays.contains(t.getDayOfWeek()))
	        .collect(Collectors.toList());
		System.out.print(((Stream<LocalDate>) allDates).count());
	}

}
