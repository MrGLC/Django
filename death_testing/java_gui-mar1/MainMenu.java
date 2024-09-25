import javax.swing.*;
import java.awt.*;

public class MainMenu {

    public static void main(String[] args) {
        JFrame frame = new JFrame("Main Menu");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);

        // Set GridBagLayout
        frame.setLayout(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();

        // Create title panel
        JPanel titlePanel = new JPanel();
        JLabel titleLabel = new JLabel("Main Menu Title");
        titlePanel.add(titleLabel);

        // Set titlePanel in the center
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.weightx = 1.0;
        gbc.weighty = 1.0;
        gbc.fill = GridBagConstraints.BOTH; // Corrected from ALL to BOTH
        frame.add(titlePanel, gbc);

        // Create buttons panel at the bottom
        JPanel buttonsPanel = new JPanel(new GridLayout(1, 3, 10, 0)); // Corrected to include hgap, vgap
        JButton btn1 = new JButton("Button 1");
        JButton btn2 = new JButton("Button 2");
        JButton btn3 = new JButton("Button 3");
        
        buttonsPanel.add(btn1);
        buttonsPanel.add(btn2);
        buttonsPanel.add(btn3);

        // Set buttonsPanel at the bottom
        gbc.gridy = 1;
        gbc.weighty = 0.1;
        frame.add(buttonsPanel, gbc);

        frame.setVisible(true);
    }
}

