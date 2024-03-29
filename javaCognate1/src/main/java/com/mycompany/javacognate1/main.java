package com.mycompany.javacognate1;

import java.awt.Desktop;
import java.awt.Dimension;
import java.awt.Toolkit;
import java.awt.print.PrinterException;
import java.io.File;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JOptionPane;



public class main extends javax.swing.JFrame {
    Database dataBase = new Database();
    
    public main() {
        initComponents(); 
        try{
        //center jframe
            Dimension dim = Toolkit.getDefaultToolkit().getScreenSize();
            this.setLocation(dim.width/2-this.getSize().width/2, dim.height/2-this.getSize().height/2);
            
            dataBase.showTables(jComboBox1);
            
            attendancePanel.setVisible(true);
            masterList.setVisible(false);
            
            
            dataBase.showRowsMaster(jTable2);
            
        }catch(Exception ex){
            System.out.println(ex);
        }
   


    }

    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        buttonGroup1 = new javax.swing.ButtonGroup();
        jPanel2 = new javax.swing.JPanel();
        attendance = new javax.swing.JPanel();
        jButton1 = new javax.swing.JButton();
        masterlistPanel = new javax.swing.JPanel();
        jButton2 = new javax.swing.JButton();
        attendancePanel = new javax.swing.JPanel();
        jComboBox1 = new javax.swing.JComboBox<>();
        jScrollPane1 = new javax.swing.JScrollPane();
        jTable1 = new javax.swing.JTable();
        print = new javax.swing.JButton();
        delete = new javax.swing.JButton();
        refresh = new javax.swing.JButton();
        masterList = new javax.swing.JPanel();
        jScrollPane2 = new javax.swing.JScrollPane();
        jTable2 = new javax.swing.JTable();
        print1 = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Attendance Face Recognition");
        setMinimumSize(new java.awt.Dimension(500, 500));
        setResizable(false);
        getContentPane().setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jPanel2.setBackground(new java.awt.Color(41, 41, 41));
        jPanel2.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        attendance.setBackground(new java.awt.Color(255, 255, 255));
        attendance.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jButton1.setBackground(new java.awt.Color(41, 41, 41));
        jButton1.setFont(new java.awt.Font("Century Gothic", 0, 14)); // NOI18N
        jButton1.setForeground(new java.awt.Color(255, 255, 255));
        jButton1.setText("Attendance");
        jButton1.setBorder(null);
        jButton1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton1ActionPerformed(evt);
            }
        });
        attendance.add(jButton1, new org.netbeans.lib.awtextra.AbsoluteConstraints(2, 2, 156, 31));

        jPanel2.add(attendance, new org.netbeans.lib.awtextra.AbsoluteConstraints(15, 12, 160, 35));

        masterlistPanel.setBackground(new java.awt.Color(41, 41, 41));
        masterlistPanel.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jButton2.setBackground(new java.awt.Color(41, 41, 41));
        jButton2.setFont(new java.awt.Font("Century Gothic", 0, 14)); // NOI18N
        jButton2.setForeground(new java.awt.Color(255, 255, 255));
        jButton2.setText("Masterlist");
        jButton2.setBorder(null);
        jButton2.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton2ActionPerformed(evt);
            }
        });
        masterlistPanel.add(jButton2, new org.netbeans.lib.awtextra.AbsoluteConstraints(2, 2, 156, 31));

        jPanel2.add(masterlistPanel, new org.netbeans.lib.awtextra.AbsoluteConstraints(190, 12, 160, 35));

        getContentPane().add(jPanel2, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 840, 60));

        attendancePanel.setBackground(new java.awt.Color(255, 255, 255));
        attendancePanel.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jComboBox1.setBackground(new java.awt.Color(76, 76, 76));
        jComboBox1.setEditable(true);
        jComboBox1.setFont(new java.awt.Font("Century Gothic", 0, 18)); // NOI18N
        jComboBox1.setForeground(new java.awt.Color(255, 255, 255));
        jComboBox1.setBorder(null);
        jComboBox1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jComboBox1ActionPerformed(evt);
            }
        });
        attendancePanel.add(jComboBox1, new org.netbeans.lib.awtextra.AbsoluteConstraints(20, 20, 200, -1));

        jTable1.setFont(new java.awt.Font("Century Gothic", 0, 18)); // NOI18N
        jTable1.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {"test", "tes"}
            },
            new String [] {
                "Name", "Time"
            }
        ) {
            Class[] types = new Class [] {
                java.lang.String.class, java.lang.String.class
            };

            public Class getColumnClass(int columnIndex) {
                return types [columnIndex];
            }
        });
        jTable1.setAlignmentX(1.0F);
        jTable1.setAlignmentY(1.0F);
        jScrollPane1.setViewportView(jTable1);

        attendancePanel.add(jScrollPane1, new org.netbeans.lib.awtextra.AbsoluteConstraints(230, 10, 600, 420));

        print.setBackground(new java.awt.Color(76, 76, 76));
        print.setFont(new java.awt.Font("Century Gothic", 0, 14)); // NOI18N
        print.setForeground(new java.awt.Color(255, 255, 255));
        print.setText("Print");
        print.setBorder(null);
        print.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                printActionPerformed(evt);
            }
        });
        attendancePanel.add(print, new org.netbeans.lib.awtextra.AbsoluteConstraints(20, 150, 200, 31));

        delete.setBackground(new java.awt.Color(153, 0, 0));
        delete.setFont(new java.awt.Font("Century Gothic", 0, 14)); // NOI18N
        delete.setForeground(new java.awt.Color(255, 255, 255));
        delete.setText("Delete");
        delete.setBorder(null);
        delete.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                deleteActionPerformed(evt);
            }
        });
        attendancePanel.add(delete, new org.netbeans.lib.awtextra.AbsoluteConstraints(20, 200, 200, 31));

        refresh.setBackground(new java.awt.Color(102, 102, 102));
        refresh.setFont(new java.awt.Font("Century Gothic", 0, 14)); // NOI18N
        refresh.setForeground(new java.awt.Color(255, 255, 255));
        refresh.setText("Refresh");
        refresh.setBorder(null);
        refresh.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                refreshActionPerformed(evt);
            }
        });
        attendancePanel.add(refresh, new org.netbeans.lib.awtextra.AbsoluteConstraints(20, 100, 200, 31));

        getContentPane().add(attendancePanel, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 60, 840, 440));

        masterList.setBackground(new java.awt.Color(255, 255, 255));
        masterList.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jTable2.setFont(new java.awt.Font("Century Gothic", 0, 18)); // NOI18N
        jTable2.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {

            },
            new String [] {
                "ID", "Name"
            }
        ) {
            Class[] types = new Class [] {
                java.lang.String.class, java.lang.String.class
            };

            public Class getColumnClass(int columnIndex) {
                return types [columnIndex];
            }
        });
        jTable2.setAlignmentX(1.0F);
        jTable2.setAlignmentY(1.0F);
        jScrollPane2.setViewportView(jTable2);

        masterList.add(jScrollPane2, new org.netbeans.lib.awtextra.AbsoluteConstraints(20, 10, 800, 330));

        print1.setBackground(new java.awt.Color(76, 76, 76));
        print1.setFont(new java.awt.Font("Century Gothic", 0, 14)); // NOI18N
        print1.setForeground(new java.awt.Color(255, 255, 255));
        print1.setText("Print master");
        print1.setBorder(null);
        print1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                print1ActionPerformed(evt);
            }
        });
        masterList.add(print1, new org.netbeans.lib.awtextra.AbsoluteConstraints(320, 360, 200, 31));

        getContentPane().add(masterList, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 60, 840, 440));

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void jComboBox1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jComboBox1ActionPerformed
        dataBase.showRows(jComboBox1.getSelectedItem().toString(), jTable1);
    }//GEN-LAST:event_jComboBox1ActionPerformed

    private void jButton1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton1ActionPerformed
        attendance.setBackground(new java.awt.Color(255, 255, 255));
        masterlistPanel.setBackground(new java.awt.Color(41, 41, 41));
        
        attendancePanel.setVisible(true);
        masterList.setVisible(false);
        
        dataBase.showRows(jComboBox1.getSelectedItem().toString(), jTable1);
    }//GEN-LAST:event_jButton1ActionPerformed

    private void jButton2ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton2ActionPerformed
        masterlistPanel.setBackground(new java.awt.Color(255, 255, 255));
        attendance.setBackground(new java.awt.Color(41, 41, 41));
        attendancePanel.setVisible(false);
        masterList.setVisible(true);
       
        dataBase.showRowsMaster(jTable2);
    }//GEN-LAST:event_jButton2ActionPerformed

    private void printActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_printActionPerformed
        try {
            jTable1.print();
        } catch (PrinterException ex) {
            Logger.getLogger(main.class.getName()).log(Level.SEVERE, null, ex);
        }
    }//GEN-LAST:event_printActionPerformed

    private void print1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_print1ActionPerformed
        try {
            jTable2.print();
        } catch (PrinterException ex) {
            Logger.getLogger(main.class.getName()).log(Level.SEVERE, null, ex);
        }
    }//GEN-LAST:event_print1ActionPerformed

    private void deleteActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_deleteActionPerformed
        int column = 0;
        int row = jTable1.getSelectedRow();
        
        if (row >= 0){
//            int result = JOptionPane.showConfirmDialog(null,"Once you delete this it cannot be undone,\n"
//                    + "Are you sure you want to delete this?", 
//                    "Attendance Face Recognition",
//                 JOptionPane.YES_NO_OPTION,
//                 JOptionPane.QUESTION_MESSAGE);
//            
//            if (result == JOptionPane.YES_OPTION){
//                String password = JOptionPane.showInputDialog(null, result, title, result, icon, selectionValues, DISPOSE_ON_CLOSE);
//			//(null, "Please enter your password", "Input", JOptionPane.QUESTION_MESSAGE );
//            }
            String value = jTable1.getModel().getValueAt(row, column).toString();
            dataBase.deleteAttendance(jComboBox1.getSelectedItem().toString(), value);
            
            dataBase.showRows(jComboBox1.getSelectedItem().toString(), jTable1);
        }else{
            JOptionPane.showMessageDialog(new Login(), "Please click the row ");
        }
//        String value = jTable1.getModel().getValueAt(row, column).toString();
//        System.out.println(value);
//        dataBase.deleteAttendance();       
    }//GEN-LAST:event_deleteActionPerformed

    private void refreshActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_refreshActionPerformed
        dataBase.showRows(jComboBox1.getSelectedItem().toString(), jTable1);
    }//GEN-LAST:event_refreshActionPerformed


    private void openFile(String file){
        try{
            File path = new File(file);
            Desktop.getDesktop().open(path);
        }catch(IOException ioe){
            System.out.println(ioe);
        }
    }
    public static void main(String args[]) {
        java.awt.EventQueue.invokeLater(new Runnable() {
            @Override
            public void run() {
                new main().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JPanel attendance;
    private javax.swing.JPanel attendancePanel;
    private javax.swing.ButtonGroup buttonGroup1;
    private javax.swing.JButton delete;
    private javax.swing.JButton jButton1;
    private javax.swing.JButton jButton2;
    private javax.swing.JComboBox<String> jComboBox1;
    private javax.swing.JPanel jPanel2;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JScrollPane jScrollPane2;
    private javax.swing.JTable jTable1;
    private javax.swing.JTable jTable2;
    private javax.swing.JPanel masterList;
    private javax.swing.JPanel masterlistPanel;
    private javax.swing.JButton print;
    private javax.swing.JButton print1;
    private javax.swing.JButton refresh;
    // End of variables declaration//GEN-END:variables
}
