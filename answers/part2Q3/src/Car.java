import java.util.ArrayList;
import java.util.List;

public class Car {

    private String manufacturer;
    private int age;


    public Car(String manufacturer, int age) {
        this.manufacturer = manufacturer;
        this.age = age;
    }

    public String getManufacturer() {
        return manufacturer;
    }

    public int getAge() {
        return age;
    }



    public static void main(String[] args) {

        Car c1 = new Car("Holden", 10);
        Car c2 = new Car("Holden", 2);
        Car c3 = new Car("Mercedes", 4);
        Car c4 = new Car("Mercedes", 2);
        Car c5 = new Car("AlphaRomeo", 2);

        List<Car> cars = new ArrayList<>();
        cars.add(c1);
        cars.add(c2);
        cars.add(c3);
        cars.add(c4);
        cars.add(c5);

        for (Car c : cars) {
            System.out.println(c.getManufacturer() + "," + c.getAge());
        }

        // Collections.sort(cars, new CarComparator());

        for (Car c : cars) {
            System.out.println(c.getManufacturer() + "," + c.getAge());
        }

    }

}

