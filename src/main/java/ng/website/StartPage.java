package ng.website;

import java.util.Arrays;
import java.util.List;

import ng.appserver.NGComponent;
import ng.appserver.NGContext;

public class StartPage extends NGComponent {

	public Page currentPage;

	public StartPage( NGContext context ) {
		super( context );
	}

	public List<Page> pages() {
		return Arrays.asList(
				new Page( "APIs", null ),
				new Page( "Components", null ),
				new Page( "WebObjects integration", null ) );
	}

	public record Page( String name, String url ) {};
}