Public Class dashboard
    Private Sub dashboard_Load(sender As Object, e As EventArgs) Handles MyBase.Load

    End Sub

    Private Sub Label8_Click(sender As Object, e As EventArgs) Handles Label8.Click

    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Employee.Show()
        Monitoring.Hide()
        attendance.Hide()
        user.Hide()
        Report.Hide()
    End Sub

    Private Sub Button3_Click(sender As Object, e As EventArgs) Handles Button3.Click
        Monitoring.Show()
        Employee.Hide()
        attendance.Hide()
        user.Hide()
        Report.Hide()
    End Sub

    Private Sub Button5_Click(sender As Object, e As EventArgs) Handles Button5.Click
        attendance.Show()
        Monitoring.Hide()
        Employee.Hide()
        user.Hide()
        Report.Hide()
    End Sub

    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click
        user.Show()
        attendance.Hide()
        Monitoring.Hide()
        Employee.Hide()
        Report.Hide()
    End Sub

    Private Sub Button6_Click(sender As Object, e As EventArgs) Handles Button6.Click
        Report.Show()
        user.Hide()
        attendance.Hide()
        Monitoring.Hide()
        Employee.Hide()
    End Sub

    Private Sub Button4_Click(sender As Object, e As EventArgs) Handles Button4.Click
        Form8.Show()


    End Sub
End Class