package ng.website;

import java.time.LocalDate;
import java.util.List;

public record BlogEntry( LocalDate date, String title, String id ) {

	/**
	 * @return The public URL for the page
	 */
	public String url() {
		return "/blog/" + id();
	}

	public static List<BlogEntry> all() {
		return List.of(
				new BlogEntry( LocalDate.of( 2022, 6, 13 ), "Work progressing nicely", "2022-06-13" ),
				new BlogEntry( LocalDate.of( 2022, 6, 10 ), "Routing mechanism", "2022-06-10" ) );
	}
}