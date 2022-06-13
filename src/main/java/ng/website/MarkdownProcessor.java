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

	public static Map<String, String> variableMap() {
		final Map<String, String> v = new HashMap<>();
		v.put( "maven.groupId", "future.group.id" );
		v.put( "maven.artifactId", "future.artifact.id" );
		v.put( "maven.version", "0.0.1-SNAPSHOT" );
		return v;
	}

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