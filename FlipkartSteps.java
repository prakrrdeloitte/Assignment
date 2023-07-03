import io.cucumber.java.en.*;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

import java.util.List;

public class FlipkartSteps {
    private WebDriver driver;

    @Given("User is on Flipkart website")
    public void user_is_on_flipkart_website() {
        // Set ChromeDriver path
        System.setProperty("webdriver.chrome.driver", "C:\Program Files\Chrome Driver\chromedriver");
        // Initialize ChromeDriver instance
        driver = new ChromeDriver();
        // Maximize the browser window
        driver.manage().window().maximize();

        // Navigate to the website
        driver.get("https://www.flipkart.com/");
    }

    @When("User navigates to Travel section")
    public void user_navigates_to_travel_section() {
        // Find and click on the Travel section
        WebElement travelSection = driver.findElement(By.xpath("//a[text()='Travel']"));
        travelSection.click();
    }

    @And("User selects round trip, dates, and locations")
    public void user_selects_round_trip_dates_and_locations() {
        // Select round trip option
        WebElement roundTripOption = driver.findElement(By.xpath("//label[text()='Round Trip']"));
        roundTripOption.click();

        // Select dates and locations
        // Add code to select dates and locations based on the specific elements on the website
    }

    @And("User clicks on search")
    public void user_clicks_on_search() {
        // Find and click on the search button
        WebElement searchButton = driver.findElement(By.xpath("//button[text()='Search']"));
        searchButton.click();
    }

    @Then("User validates the total price for flights")
    public void user_validates_the_total_price_for_flights() {
        // Find all flight prices
        List<WebElement> flightPrices = driver.findElements(By.xpath("//span[@class='flightPrice']"));

        // Calculate the sum of flight prices
        double totalPrice = 0.0;
        for (WebElement flightPrice : flightPrices) {
            String priceStr = flightPrice.getText().replaceAll("[^\\d.]", "");
            double price = Double.parseDouble(priceStr);
            totalPrice += price;
        }

        // Compare the total price with the sum of flight prices
        // Add assertions or further actions as needed

        // Close the browser
        driver.quit();
    }
}
