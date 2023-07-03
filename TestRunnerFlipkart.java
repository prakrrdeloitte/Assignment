import io.cucumber.testng.AbstractTestNGCucumberTests;
import io.cucumber.testng.CucumberOptions;

@CucumberOptions(features = "/Users/prakrr/PycharmProjects/Udemy/flipkart.feature",
        glue = "/Users/prakrr/PycharmProjects/Udemy/FlipkartSteps.java")
public class TestRunner extends AbstractTestNGCucumberTests {
}
