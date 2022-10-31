package com.mycompany.javacognate1;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Collections;
import javax.swing.JComboBox;
import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;

public class Database {
    private Connection conn;
    private  Statement state;

// connection query
    private Statement getConnected(){
        
        String url = "jdbc:mysql://localhost/";
        String dbName = "cognate1";
        String driver = "com.mysql.jdbc.Driver";
        String userName = "root";
        String password = "";
        
        try{
            Class.forName(driver);
            conn = DriverManager.getConnection(url+dbName,userName,password);
            state = conn.createStatement();
            System.out.println("Connected to database");
            
            return state;
            
        }catch(Exception e){
            System.out.println(e);
            System.out.println("Could not connect database");
            return null;
        }
        
    }
 
 //Login Query
    public boolean login(String tableName, String username,String password){
        try{
            String query = "SELECT `ID` FROM " + 
                    tableName + " WHERE username='"+ username + "' AND password='" + password + "'";
            ResultSet result =  getConnected().executeQuery(query);
            int ID = 0;
            while(result.next()){
                ID = result.getInt("ID");
            }
            if(ID != 0){
                System.out.println("wow");
                conn.close();
                return true;
            }else{
                System.out.println("nope");
                conn.close();
                return false;
            }
            
            
        }catch(Exception e){
            System.out.println(e);
            return false;
        } 
    }
 
// SHOW OF ALL TABLES
    public void showTables(JComboBox jComboBox1){
        try{
            
            ArrayList<String> tableNames = new ArrayList<String>();
            
            String query = "SHOW TABLES";
            ResultSet result = getConnected().executeQuery(query);
            while(result.next()){
                tableNames.add(result.getString(1));
            }

            tableNames.remove("admin");
            tableNames.remove("masterlist");
            
            conn.close();
            Collections.sort(tableNames, Collections.reverseOrder()); 
            
            
            jComboBox1.removeAllItems();
            tableNames.forEach(item->jComboBox1.addItem(item));
 
            
        }catch(Exception e){
            System.out.println(e);
        }
    }
 
// SHOW ALL ROWS IN SPECIFIC TABLES
    public void showRows(String date,JTable table){
            try{
            
            DefaultTableModel tblmodel = (DefaultTableModel)table.getModel();
            tblmodel.setRowCount(0);
            String query = "SELECT * FROM `" + date + "`";
            ResultSet result = getConnected().executeQuery(query);
            
            while(result.next()){
                String data[] = {result.getString("Name"),result.getString("Time")};
                tblmodel.addRow(data);
            }            
            conn.close();      
        }catch(Exception e){
            System.out.println(e);
 
        } 
    }
//    SHOW ALL MASTELIST
        public void showRowsMaster(JTable table){
        try{
            
            DefaultTableModel tblmodel = (DefaultTableModel)table.getModel();
            tblmodel.setRowCount(0);
            
            String query = "SELECT * FROM `masterlist`";
            ResultSet result = getConnected().executeQuery(query);
            
            while(result.next()){
                String data[] = {result.getString("ID"),result.getString("Name")};
                tblmodel.addRow(data);
            }            
            conn.close();     
        }catch(Exception e){
            System.out.println(e);
        }
    }
        
//  delete Attendace      
    public void deleteAttendance(String date, String Name){
        
          try{       
            String query = "DELETE FROM `" + date + "` WHERE Name='" + Name + "'";       
            System.out.println(getConnected().executeUpdate(query));
            conn.close();
   
        }catch(Exception e){
            System.out.println(e);

        }
        
    }
    
  
}
