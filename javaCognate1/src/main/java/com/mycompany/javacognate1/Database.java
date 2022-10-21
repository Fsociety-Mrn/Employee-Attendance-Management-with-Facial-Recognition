package com.mycompany.javacognate1;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Collections;

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
    public ArrayList<String> showTables(){
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
            return tableNames;
            
        }catch(Exception e){
            System.out.println(e);
            return null;
        }
    }
 
// SHOW ALL ROWS IN SPECIFIC TABLES
    public ArrayList<String> showRows(String date){
        try{
            
            ArrayList<String> tableNames = new ArrayList<String>();
            
            String query = "SELECT * FROM `" + date + "`";
            ResultSet result = getConnected().executeQuery(query);
            
            while(result.next()){
                  tableNames.add(result.getString("Name"));
                  tableNames.add(result.getString("Time"));
            }            
            conn.close();
            return tableNames;        
        }catch(Exception e){
            System.out.println(e);
            return null;
        }
    }
  
}
