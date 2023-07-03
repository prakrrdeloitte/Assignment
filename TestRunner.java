import io.cucumber.testng.AbstractTestNGCucumberTests;
import io.cucumber.testng.CucumberOptions;

@CucumberOptions(features = "path_to_feature_file/weather_shopper.feature",
        glue = "path_to_step_definition_file/WeatherShopperSteps")
public class TestRunner extends AbstractTestNGCucumberTests {
}
