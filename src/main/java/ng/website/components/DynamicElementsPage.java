package ng.website.components;

import java.util.List;

import ng.appserver.NGContext;
import ng.appserver.templating.NGComponent;
import ng.appserver.templating.NGDynamicElementDescription;
import ng.appserver.templating.NGDynamicElementDescription.NGBindingDescription;

public class DynamicElementsPage extends NGComponent {

	/**
	 * The text NGDynamicElementDescription uses for elements that have no documentation yet
	 */
	private static final String UNDOCUMENTED_TEXT = "Documentation forthcoming";

	public NGDynamicElementDescription current;
	public NGBindingDescription currentBinding;
	public String currentAlias;

	public DynamicElementsPage( NGContext context ) {
		super( context );
	}

	public List<NGDynamicElementDescription> all() {
		return NGDynamicElementDescription.all();
	}

	public String currentAlias() {
		return tagMarkup( currentAlias );
	}

	/**
	 * @return The element's first alias as tag markup, for places where only one alias is shown
	 */
	public String currentPrimaryAlias() {
		return tagMarkup( current.aliases().getFirst() );
	}

	private String tagMarkup( final String alias ) {
		if( current.isContainerElement() ) {
			return "<wo:%s>".formatted( alias );
		}

		return "<wo:%s />".formatted( alias );
	}

	/**
	 * @return The element's primary tag, used to name it in the page index
	 */
	public String currentTag() {
		return "wo:" + current.aliases().getFirst();
	}

	public String currentAnchorID() {
		return current.elementClass().getSimpleName();
	}

	public String currentAnchor() {
		return "#" + currentAnchorID();
	}

	public boolean currentIsDocumented() {
		return !UNDOCUMENTED_TEXT.equals( current.text() );
	}

	/**
	 * @return A class name that mutes undocumented elements in the page index
	 */
	public String currentIndexClass() {
		return currentIsDocumented() ? null : "undocumented";
	}

	public boolean currentHasBindings() {
		return !current.bindings().isEmpty();
	}

	/**
	 * @return The simple name of the binding's type, or null if it isn't declared
	 */
	public String currentBindingType() {
		final Class<?> bindingClass = currentBinding.bindingClass();
		return bindingClass != null ? bindingClass.getSimpleName() : null;
	}
}
