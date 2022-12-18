Imports MySqlConnector


Public Class user

    Dim ID As String


    Private Sub Button5_Click(sender As Object, e As EventArgs) Handles Button5.Click
        Me.Close()
    End Sub
    Sub DatatableDat()
        Try
            Dim bindingSource As New BindingSource
            Dim dataTable As New DataTable



            openCon() ''connection 

            mysqlCommand.Connection = con
            mysqlCommand.CommandText = "SELECT * FROM `admin`;"
            mysqlAdapter.SelectCommand = mysqlCommand

            mysqlAdapter.Fill(dataTable)
            bindingSource.DataSource = dataTable
            DataGridView1.DataSource = bindingSource
            mysqlAdapter.Update(dataTable)

            con.Close()

        Catch ex As Exception
            MessageBox.Show(ex.ToString)
            con.Close()
        End Try
    End Sub
    Public Sub Insert()
        Dim bindingSource As New BindingSource
        Dim dataTable As New DataTable

        Try


            openCon() ''connection 

            Dim aso As String = "INSERT INTO `admin` (`Position`, `Full Name`, `username`, password) VALUES ('" + ComboBox2.Text + "', '" + TextBox4.Text + "', '" + TextBox1.Text + "', '" + TextBox2.Text + "');"


            mysqlCommand.Connection = con
            ''mysqlCommand.CommandText = "INSERT INTO 'admin' (Position, Full Name, username, password) " +
            '' "VALUES ('" + ComboBox2.Text + "', '" + TextBox4.Text + "', '" + TextBox1.Text + "', '" + TextBox2.Text + "');"
            mysqlCommand.CommandText = aso
            mysqlAdapter.SelectCommand = mysqlCommand

            ''dataTable.Clear() ''dataset
            mysqlAdapter.Fill(dataTable)


            bindingSource.DataSource = dataTable
            DataGridView1.DataSource = bindingSource
            mysqlAdapter.Update(dataTable)
            MessageBox.Show("Data has been updated")

            con.Close()

            DatatableDat()
            TextBox1.Text = ""
            TextBox2.Text = ""
            TextBox4.Text = ""
            ComboBox2.Text = ""
            ''Button1.Enabled = False

        Catch ex As Exception

            MessageBox.Show(ex.ToString)
            con.Close()
            DatatableDat()
        End Try


    End Sub
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        ''Insert()
        Me.Enabled = False
        insertUser.Show()
    End Sub

    Private Sub user_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        DatatableDat()
        ComboBox1.SelectedIndex = 0
    End Sub

    Private Sub TextBox3_TextChanged(sender As Object, e As EventArgs) Handles TextBox3.TextChanged
        Dim bindingSource As New BindingSource
        Dim dataTable As New DataTable

        Try

            If TextBox3.Text = "" Then
                DatatableDat()
            Else
                openCon() ''connection 

                mysqlCommand.Connection = con
                mysqlCommand.CommandText = "SELECT * FROM `admin` WHERE `Full Name` like '%" & TextBox3.Text & "%';"
                mysqlAdapter.SelectCommand = mysqlCommand

                mysqlAdapter.Fill(dataTable)
                bindingSource.DataSource = dataTable
                DataGridView1.DataSource = bindingSource
                mysqlAdapter.Update(dataTable)

                con.Close()
            End If

        Catch ex As Exception

            ''MessageBox.Show(ex.ToString)
            con.Close()
            DatatableDat()

        End Try
    End Sub

    Private Sub DataGridView1_CellContentClick(sender As Object, e As DataGridViewCellEventArgs) Handles DataGridView1.CellContentClick
        If e.RowIndex >= 0 Then
            Dim row As DataGridViewRow = DataGridView1.Rows(e.RowIndex)
            ID = row.Cells(0).Value.ToString
            ComboBox2.Text = row.Cells(1).Value.ToString
            TextBox4.Text = row.Cells(2).Value.ToString
            TextBox1.Text = row.Cells(3).Value.ToString
            TextBox2.Text = row.Cells(4).Value.ToString
            Button1.Enabled = True
        End If
    End Sub

    Private Sub ComboBox1_SelectedIndexChanged(sender As Object, e As EventArgs) Handles ComboBox1.SelectedIndexChanged
        If ComboBox1.Text = "All" Then
            DatatableDat()
        Else
            Dim bindingSource As New BindingSource
            Dim dataTable As New DataTable

            Try
                openCon() ''connection 

                mysqlCommand.Connection = con
                mysqlCommand.CommandText = "SELECT * FROM `admin` WHERE `Position` = '" + ComboBox1.Text + "';"
                mysqlAdapter.SelectCommand = mysqlCommand

                mysqlAdapter.Fill(dataTable)
                bindingSource.DataSource = dataTable
                DataGridView1.DataSource = bindingSource
                mysqlAdapter.Update(dataTable)

                con.Close()

            Catch ex As Exception
                MessageBox.Show(ex.ToString)
                con.Close()
            End Try
        End If
    End Sub

    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click

        ''Update()

        Me.Enabled = False

        updateUser.Show()
    End Sub
    Public Sub Update()
        Dim bindingSource As New BindingSource
        Dim dataTable As New DataTable

        Try

            openCon() ''connection 

            mysqlCommand.Connection = con
            mysqlCommand.CommandText = "UPDATE `admin` SET `Position` = '" + ComboBox2.Text + "', `Full Name`='" + TextBox4.Text + "', `username` = '" + TextBox1.Text + "', `password` = '" + TextBox2.Text + "'WHERE `ID` = '" + ID + "';"
            mysqlAdapter.SelectCommand = mysqlCommand

            ''dataTable.Clear() ''dataset
            mysqlAdapter.Fill(dataTable)


            bindingSource.DataSource = dataTable
            DataGridView1.DataSource = bindingSource
            mysqlAdapter.Update(dataTable)
            MessageBox.Show("Data has been updated")

            con.Close()

            DatatableDat()
            TextBox1.Text = ""
            TextBox2.Text = ""
            TextBox4.Text = ""
            ComboBox2.Text = ""
            ''Button1.Enabled = False

        Catch ex As Exception

            MessageBox.Show(ex.ToString)
            con.Close()
            DatatableDat()
        End Try

    End Sub

    Private Sub Button3_Click(sender As Object, e As EventArgs) Handles Button3.Click
        ComboBox2.Text = ""
        TextBox4.Text = ""
        TextBox1.Text = ""
        TextBox2.Text = ""
    End Sub
End Class
