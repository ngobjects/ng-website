package ng.website.components;

import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

import com.vladsch.flexmark.html.HtmlRenderer;
import com.vladsch.flexmark.parser.Parser;
import com.vladsch.flexmark.util.data.MutableDataSet;

import ng.appserver.NGApplication;
import ng.appserver.NGContext;
import ng.appserver.templating.NGComponent;
import ng.appserver.templating.definitions.NGElementAPI;
import ng.appserver.templating.NGElementManager.DeclaredElement;

/**
 * The reference for the framework's own elements, read from ng itself: every element it publishes (an .apiext in
 * ng/ng/elements), each one's API from that file and its tags from the namespace's tag aliases. Nothing here lists or describes an element by hand.
 */

public class DynamicElementsPage extends NGComponent {

	/**
	 * The namespace whose elements the page documents: the framework's own
	 */
	private static final String FRAMEWORK_NAMESPACE = "ng";

	/**
	 * Renders the Markdown in element and binding docs. Shared: flexmark's parser and renderer are thread safe.
	 */
	private static final Parser MARKDOWN_PARSER;
	private static final HtmlRenderer MARKDOWN_RENDERER;

	static {
		final MutableDataSet options = new MutableDataSet();
		MARKDOWN_PARSER = Parser.builder( options ).build();
		MARKDOWN_RENDERER = HtmlRenderer.builder( options ).build();
	}

	public Entry current;
	public NGElementAPI.Binding currentBinding;
	public String currentTag;

	private List<Entry> _all;

	public DynamicElementsPage( NGContext context ) {
		super( context );
	}

	/**
	 * @return The framework's declared elements, by primary tag
	 */
	public List<Entry> all() {
		if( _all == null ) {
			_all = NGApplication.application()
					.elementManager()
					.declaredElements()
					.stream()
					.filter( e -> FRAMEWORK_NAMESPACE.equals( e.namespace() ) )
					.map( e -> new Entry( e, e.api(), NGApplication.application().elementManager().tagsFor( e.name() ) ) )
					.sorted( Comparator.comparing( e -> primaryTag( e ).toLowerCase() ) )
					.toList();
		}

		return _all;
	}

	/**
	 * @return The tag an element is usually written with: its first tag, or its name when it has none
	 */
	private static String primaryTag( final Entry entry ) {
		return entry.tags().isEmpty() ? entry.element().name() : entry.tags().getFirst();
	}

	/**
	 * @return The element's tags, its name when it has none
	 */
	public List<String> currentTags() {
		return current.tags().isEmpty() ? List.of( current.element().name() ) : current.tags();
	}

	/**
	 * @return The tag being iterated as markup, open for a container, self-closing otherwise
	 */
	public String currentTagMarkup() {
		return tagMarkup( currentTag );
	}

	/**
	 * @return The element's primary tag as markup, for places where only one is shown
	 */
	public String currentPrimaryTagMarkup() {
		return tagMarkup( primaryTag( current ) );
	}

	private String tagMarkup( final String tag ) {
		return currentIsContainer() ? "<wo:%s>".formatted( tag ) : "<wo:%s />".formatted( tag );
	}

	/**
	 * @return The element's primary tag, naming it in the page index
	 */
	public String currentIndexTag() {
		return "wo:" + primaryTag( current );
	}

	public String currentAnchorID() {
		return current.element().name();
	}

	public String currentAnchor() {
		return "#" + currentAnchorID();
	}

	public boolean currentIsContainer() {
		return current.api() != null && current.api().wrapsContent();
	}

	public boolean currentIsDocumented() {
		return current.api() != null && current.api().doc() != null;
	}

	/**
	 * @return A class name that mutes undocumented elements in the page index
	 */
	public String currentIndexClass() {
		return currentIsDocumented() ? null : "undocumented";
	}

	/**
	 * @return The element's implementation class, or null for a template-only component
	 */
	public String currentClassName() {
		return current.element().elementClass() != null ? current.element().elementClass().getName() : null;
	}

	public String currentDocHTML() {
		return markdown( current.api().doc() );
	}

	public boolean currentHasBindings() {
		return current.api() != null && !current.api().bindings().isEmpty();
	}

	/**
	 * @return The binding's types, simple names: what it reads, and (after an arrow) what it writes back
	 */
	public String currentBindingTypes() {
		final String pulled = simpleNames( currentBinding.pullTypes() );
		final String pushed = simpleNames( currentBinding.pushTypes() );

		if( pushed.isEmpty() ) {
			return pulled;
		}

		return pulled.isEmpty() ? "→ " + pushed : pulled + " → " + pushed;
	}

	/**
	 * @return What the element does with the binding: reads it, writes to it, or both
	 */
	public String currentBindingDirection() {
		if( currentBinding.isPulled() && currentBinding.isPushed() ) {
			return "read and written";
		}

		return currentBinding.isPushed() ? "written" : "read";
	}

	public String currentBindingDocHTML() {
		return currentBinding.doc() != null ? markdown( currentBinding.doc() ) : null;
	}

	public String currentBindingDeprecatedHTML() {
		return currentBinding.deprecated() != null && !currentBinding.deprecated().isEmpty() ? markdown( currentBinding.deprecated() ) : null;
	}

	private static String simpleNames( final List<String> classNames ) {
		return classNames.stream().map( n -> n.substring( n.lastIndexOf( '.' ) + 1 ) ).collect( Collectors.joining( " | " ) );
	}

	private static String markdown( final String markdown ) {
		return MARKDOWN_RENDERER.render( MARKDOWN_PARSER.parse( markdown ) );
	}

	/**
	 * A declared element and its API (null when it has no .apiext file)
	 */
	public record Entry( DeclaredElement element, NGElementAPI api, List<String> tags ) {}
}
