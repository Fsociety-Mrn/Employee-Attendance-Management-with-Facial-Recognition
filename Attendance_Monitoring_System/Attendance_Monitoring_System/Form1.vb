Public Class login
    Private Sub Button2_Click(sender As Object, e As EventArgs)
        Me.Close()

    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Dim username As String
        Dim password As String
        username = txtUser.Text
        password = txtPass.Text
        If (username.Equals("admin") And password.Equals("admin")) Then
            MessageBox.Show("Login Success", "Information", MessageBoxButtons.OK, MessageBoxIcon.Information)
            dashboard.Show()
            Me.Hide()


        ElseIf (txtUser.Text = "admin" And txtPass.Text <> "admin") Then
            MessageBox.Show("Only username is correct!", "Information", MessageBoxButtons.OK, MessageBoxIcon.Information)

        ElseIf (txtUser.Text <> "admin" And txtPass.Text = "admin") Then
            MessageBox.Show("Only Password is correct!", "Information", MessageBoxButtons.OK, MessageBoxIcon.Information)
        Else
            MessageBox.Show("Incorrect Username and Password", "Information", MessageBoxButtons.OK, MessageBoxIcon.Error)
        End If
    End Sub

    Private Sub Button3_Click(sender As Object, e As EventArgs) Handles Button3.Click
        Application.Exit()

    End Sub
End Class
