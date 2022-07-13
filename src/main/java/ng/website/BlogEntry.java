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

	/**
	 * @return All of our blog entries
	 */
	public static List<BlogEntry> allBlogEntries() {
		return List.of(
				new BlogEntry( LocalDate.of( 2022, 7, 12 ), "We have a nice exception page!", "2022-07-12" ),
				new BlogEntry( LocalDate.of( 2022, 6, 25 ), "Looking for a name", "2022-06-25" ) );
	}
}