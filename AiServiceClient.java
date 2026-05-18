import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;

public class AiServiceClient {

    public static void main(String[] args) {

        try {
            URL url = new URL("http://localhost:5000/ai/recommend");

            HttpURLConnection conn = (HttpURLConnection) url.openConnection();

            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "application/json");
            conn.setDoOutput(true);

            String jsonInput = """
            {
                "description": "Financial risk due to market volatility",
                "category": "Finance"
            }
            """;

            try(OutputStream os = conn.getOutputStream()) {
                byte[] input = jsonInput.getBytes("utf-8");
                os.write(input, 0, input.length);
            }

            BufferedReader br = new BufferedReader(
                    new InputStreamReader(conn.getInputStream(), "utf-8"));

            StringBuilder response = new StringBuilder();
            String responseLine;

            while ((responseLine = br.readLine()) != null) {
                response.append(responseLine.trim());
            }

            System.out.println("Response:");
            System.out.println(response.toString());

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}