import io.cucumber.java.en.*;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class WeatherShopperSteps {
    private WebDriver driver;

    @Given("User is on Weather Shopper website")
    public void user_is_on_weather_shopper_website() {
        // Set ChromeDriver path
        System.setProperty("webdriver.chrome.driver", "C:\Program Files\Chrome Driver\chromedriver"");
        // Initialize ChromeDriver instance
        driver = new ChromeDriver();
        // Maximize the browser window
        driver.manage().window().maximize();

        // Navigate to the website
        driver.get("https://weathershopper.pythonanywhere.com/");
    }

    @When("User gets the temperature")
    public void user_gets_the_temperature() {
        // Get the temperature
        WebElement temperatureElement = driver.findElement(By.id("temperature"));
        int temperature = Integer.parseInt(temperatureElement.getText().replaceAll("\\D+", ""));
        // Store the temperature value for later use
        // You can use an instance variable or a test context variable to store the temperature value
    }

    @And("User chooses to buy sunscreen or moisturizer based on the temperature")
    public void user_chooses_product_based_on_temperature() {
        // Based on temperature, choose to buy sunscreen or moisturizer
        WebElement buyButton;
        // Use the stored temperature value to make a decision
        int temperature = 0; // Replace with the actual stored temperature value
        if (temperature > 34) {
            buyButton = driver.findElement(By.id("buy_sunscreen"));
        } else {
            buyButton = driver.findElement(By.id("buy_moisturizer"));
        }
        buyButton.click();
    }

    @And("User reads instructions and adds the product accordingly")
    public void user_reads_instructions_and_adds_product_accordingly() {
        // Read instructions using info button and add the product accordingly
        WebElement infoButton = driver.findElement(By.id("more-info"));
        infoButton.click();
        // Read the instructions and add the product accordingly
    }

    @And("User verifies the cart")
    public void user_verifies_the_cart() {
        // Verify the cart
    }

    @And("User makes a payment")
    public void user_makes_a_payment() {
        // Make a payment
    }

    @Then("User completes the purchase")
    public void user_completes_the_purchase() {
        // Add assertions or further actions as needed

        // Close the browser
        driver.quit();
    }
}
