import javax.swing.*;

public class SimpleGUI {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Simple GUI");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(200, 100);
            JLabel label = new JLabel("Hello, GUI!", SwingConstants.CENTER);
            frame.add(label);
            frame.setLocationRelativeTo(null); // Center the window
            frame.setVisible(true);
        });
    }
}

