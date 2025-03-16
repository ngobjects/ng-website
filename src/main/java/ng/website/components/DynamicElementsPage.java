package ng.website.components;

import java.util.List;

import ng.appserver.NGComponent;
import ng.appserver.NGContext;
import ng.appserver.templating.NGDynamicElementDescription;
import ng.appserver.templating.NGDynamicElementDescription.NGBindingDescription;

public class DynamicElementsPage extends NGComponent {

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
		if( current.isContainerElement() ) {
			return "<wo:%s>".formatted( currentAlias, currentAlias );
		}

		return "<wo:%s />".formatted( currentAlias );
	}

	public String currentAnchor() {
		return "#" + current.elementClass().getSimpleName();
	}

	public boolean currentHasBindings() {
		return !current.bindings().isEmpty();
	}
}