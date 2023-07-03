import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

public class WeatherShopperTest {
    private WebDriver driver;

    @BeforeClass
    public void setUp() {
        // Set ChromeDriver path
        System.setProperty("webdriver.chrome.driver", "C:\Program Files\Chrome Driver\chromedriver");
        // Initialize ChromeDriver instance
        driver = new ChromeDriver();
        // Maximize the browser window
        driver.manage().window().maximize();
    }

    @Test
    public void testWeatherShopper() {
        // Navigate to the website
        driver.get("https://weathershopper.pythonanywhere.com/");

        // Get the temperature
        WebElement temperatureElement = driver.findElement(By.id("temperature"));
        int temperature = Integer.parseInt(temperatureElement.getText().replaceAll("\\D+", ""));

        // Based on temperature, choose to buy sunscreen or moisturizer
        WebElement buyButton;
        if (temperature > 34) {
            buyButton = driver.findElement(By.id("buy_sunscreen"));
        } else {
            buyButton = driver.findElement(By.id("buy_moisturizer"));
        }
        buyButton.click();

        // Read instructions using info button and add product accordingly
        WebElement infoButton = driver.findElement(By.id("more-info"));
        infoButton.click();
        // Read the instructions and add the product accordingly

        // Verify the cart

        // Make a payment

        // Add assertions or further actions as needed
    }

    @AfterClass
    public void tearDown() {
        // Close the browser
        driver.quit();
    }
}
