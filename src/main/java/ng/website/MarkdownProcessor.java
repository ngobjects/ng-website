package ng.website;

import java.util.HashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Allows us to use substitution variables in our markdown templates
 *
 * Variables are consumed by the template using the syntax ${variableName}
 */

public class MarkdownProcessor {

	private static final Pattern VAR_PATTERN = Pattern.compile( "\\$\\{.*?\\}" );

	private static Map<String, String> variableMap() {
		final Map<String, String> v = new HashMap<>();
		// The framework's current release, as used in the docs' code samples. Named so they don't collide with ${...} placeholders shown in those samples.
		v.put( "ng.groupId", "is.rebbi.ng" );
		v.put( "ng.release", "0.1.6" );
		v.put( "vermilingua.release", "1.2.0" );
		v.put( "java.release", "25" );
		return v;
	}

	/**
	 * @return templateString where variables have been replaced with their corresponding values
	 */
	public static String process( final String templateString ) {
		String result = templateString;
		Matcher m = VAR_PATTERN.matcher( templateString );

		while( m.find() ) {
			String group = m.group();
			String key = group.substring( 2, group.length() - 1 );
			Object value = variableMap().get( key );

			if( value == null ) {
				value = "--UNSET VARIABLE " + key + "--";
			}
			else {
				result = result.replace( group, value.toString() );

			}
		}

		return result;
	}
}