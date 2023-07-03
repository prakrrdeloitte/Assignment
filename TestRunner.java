import io.cucumber.testng.AbstractTestNGCucumberTests;
import io.cucumber.testng.CucumberOptions;

@CucumberOptions(features = "/Users/prakrr/PycharmProjects/Udemy/weather_shopper.feature",
        glue = "/Users/prakrr/PycharmProjects/Udemy/WeatherShopperSteps.java")
public class TestRunner extends AbstractTestNGCucumberTests {
}
