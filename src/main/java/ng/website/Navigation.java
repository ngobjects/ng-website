package ng.website;

import java.util.List;
import java.util.stream.Stream;

/**
 * The site's navigation tree, shown on every page. Sections hold nodes, and a node can hold child nodes.
 *
 * This is the one place to rearrange the site's structure.
 */

public class Navigation {

	/**
	 * A titled group of nodes in the navigation
	 */
	public record Section( String title, List<Node> nodes ) {}

	/**
	 * A link in the navigation, or (when url is null) a label grouping its children
	 */
	public record Node( String name, String url, List<Node> children ) {

		public static Node of( final Page page ) {
			return new Node( page.name(), page.url(), List.of() );
		}

		public boolean isLink() {
			return url != null;
		}

		public boolean hasChildren() {
			return !children.isEmpty();
		}
	}

	/**
	 * @return The sections of the navigation, in display order
	 */
	public static List<Section> sections() {
		return List.of(
				new Section( "Start here", nodes( "getting-started", "setting-up" ) ),
				new Section( "Guides", nodes( "creating-a-component", "templating", "component-actions", "partial-page-updates", "sessions", "resources", "routing", "creating-a-dynamic-element" ) ),
				new Section( "Running your app", nodes( "configuration", "development-tools", "deployment" ) ),
				new Section( "Coming from WebObjects", nodes( "wo-integration" ) ),
				new Section( "Reference", nodes( "dynamic-elements", "plugins", "glossary" ) ) );
	}

	/**
	 * @return Navigation nodes for the pages with the given ids, in order
	 */
	private static List<Node> nodes( final String... pageIds ) {
		return Stream.of( pageIds ).map( Page::byId ).map( Node::of ).toList();
	}

	/**
	 * @return The names leading to the page at the given url (section, any group, then the page), or an empty list if it isn't in the navigation
	 */
	public static List<String> trail( final String url ) {
		for( final Section section : sections() ) {
			for( final Node node : section.nodes() ) {
				if( url.equals( node.url() ) ) {
					return List.of( section.title(), node.name() );
				}

				for( final Node child : node.children() ) {
					if( url.equals( child.url() ) ) {
						return List.of( section.title(), node.name(), child.name() );
					}
				}
			}
		}

		return List.of();
	}
}
