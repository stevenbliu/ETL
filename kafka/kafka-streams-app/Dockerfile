FROM openjdk:11-jre-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the entire project into the container (make sure your local directory has the pom.xml file)
COPY . /app

# Install Maven to build the project inside the container
RUN apt-get update && apt-get install -y maven

# Ensure the pom.xml exists in the /app directory before running mvn command
RUN ls -al /app

# Build the Kafka Streams application (use the same command as you would locally)
RUN mvn clean install

# Expose the port that your Kafka Streams app will run on (adjust if needed)
EXPOSE 8080

# Define the entry point to run the Kafka Streams application
CMD ["java", "-jar", "target/your-kafka-streams-app.jar"]
