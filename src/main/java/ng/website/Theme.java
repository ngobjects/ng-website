package ng.website;

import java.time.Duration;

import ng.appserver.NGContext;
import ng.appserver.http.NGCookie;
import ng.appserver.http.NGRequest;
import ng.appserver.http.NGResponse;
import ng.appserver.http.NGResponses;

/**
 * The site's look while the framework's name is being decided: engifer (ginger) or glytta (jellyfish).
 * A visitor picks one at /theme/{name}, which remembers it in a cookie.
 */

public enum Theme {

	glytta,
	engifer;

	private static final Theme DEFAULT = glytta;

	private static final String COOKIE_NAME = "theme";

	public boolean isGlytta() {
		return this == glytta;
	}

	public boolean isEngifer() {
		return this == engifer;
	}

	/**
	 * @return The theme the visitor picked, or the default
	 */
	public static Theme of( final NGContext context ) {
		return parse( context.request().cookieValueForKey( COOKIE_NAME ) );
	}

	private static Theme parse( final String name ) {
		for( Theme theme : values() ) {
			if( theme.name().equals( name ) ) {
				return theme;
			}
		}

		return DEFAULT;
	}

	/**
	 * Handles /theme/{name}?return={path}: remembers the theme and sends the visitor back to the page they were on
	 */
	public static NGResponse switchTo( final NGRequest request, final String name ) {
		final String returnPath = request.formValueForKey( "return" );
		final boolean safe = returnPath != null && returnPath.startsWith( "/" ) && !returnPath.startsWith( "//" );

		final NGResponse response = NGResponses.of( 302, "" );
		response.setHeader( "Location", safe ? returnPath : "/" );
		response.addCookie( new NGCookie( COOKIE_NAME, parse( name ).name(), Duration.ofDays( 365 ) ) );
		return response;
	}
}
