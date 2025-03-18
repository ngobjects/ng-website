package ng.website.components;

import java.util.ArrayList;
import java.util.List;

import ng.appserver.NGActionResults;
import ng.appserver.NGContext;
import ng.appserver.templating.NGComponent;

public class PetsPage extends NGComponent {

	public List<Pet> pets = new ArrayList<>();
	public Pet currentPet;
	public String myName;

	public PetsPage( NGContext context ) {
		super( context );
	}

	public NGActionResults clearNames() {
		pets = new ArrayList<>();
		return null;
	}

	public NGActionResults addMyName() {
		Pet pet = new Cat();
		pet.name = myName;
		pets.add( pet );
		return null;
	}

	public NGActionResults petCurrentPet() {
		currentPet.pet();
		return null;
	}

	public static class Pet {
		public String name;

		public void pet() {
			System.out.println( "Whererer!" );
		}
	}

	public static class Dog extends Pet {
		@Override
		public void pet() {
			System.out.println( "Voff!" );
		}
	}

	public static class Cat extends Pet {

		@Override
		public void pet() {
			System.out.println( "Mjá mjá" );
		}

	}
}