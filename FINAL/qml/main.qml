import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import Qt.labs.calendar 1.0
import Qt.labs.qmlmodels 1.0
import "./controls"
import "controls"
Window {
    id: window
    width: 640
    height: 480
    visible: true
    color: "#001e222a"
    title: qsTr("Hello World")

    Rectangle {
        id: bg
        color: "#2c313c"
        border.color: "#4c5467"
        border.width: 0
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.rightMargin: 10
        anchors.leftMargin: 10
        anchors.bottomMargin: 10
        anchors.topMargin: 10

        Rectangle {
            id: appContainer
            color: "#00000000"
            anchors.fill: parent
            anchors.rightMargin: 1
            anchors.leftMargin: 1
            anchors.bottomMargin: 1
            anchors.topMargin: 1


            Rectangle {
                id: topBar
                height: 70
                color: "#1e222a"
                border.color: "#1f222a"
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.rightMargin: 0
                anchors.leftMargin: 0
                anchors.topMargin: 0

                CustomBtn {
                    id: toggleButton
                    width: 70
                    height: 70
                    opacity: 1
                    text: qsTr("Button")
                    anchors.left: parent.left
                    anchors.top: parent.top
                    toggleBtnIcon: "../images/svg/view_headline-24px.svg"
                    display: AbstractButton.IconOnly
                    anchors.topMargin: 0
                    anchors.leftMargin: 0
                }

                Rectangle {
                    id: topBarDescription
                    y: 39
                    height: 31
                    color: "#464e5f"
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.bottom: parent.bottom
                    anchors.rightMargin: 0
                    anchors.leftMargin: 71
                    anchors.bottomMargin: 0

                    Label {
                        id: status
                        x: 435
                        width: 112
                        color: "#b6b6b6"
                        text: qsTr("سوابق مراجعات")
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        horizontalAlignment: Text.AlignRight
                        verticalAlignment: Text.AlignVCenter
                        anchors.rightMargin: 0
                        anchors.bottomMargin: 0
                        anchors.topMargin: 0
                    }

                    Label {
                        id: dateLabel
                        x: 0
                        y: 0
                        width: 137
                        height: 31
                        color: "#c1c1c1"
                        text: qsTr("دوشنبه ۱۴۰۰/۰۴/۲۷")
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                    }
                }

                Rectangle {
                    id: titleBar
                    y: 0
                    height: 38
                    color: "#00000000"
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.bottom: parent.bottom
                    anchors.rightMargin: 105
                    anchors.leftMargin: 71
                    anchors.bottomMargin: 32

                    Image {
                        id: appIcon
                        width: 28
                        opacity: 1
                        anchors.left: parent.left
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        source: "../images/svg/record_voice_over-24px.svg"
                        clip: true
                        autoTransform: false
                        mipmap: false
                        anchors.topMargin: 2
                        anchors.bottomMargin: 2
                        anchors.leftMargin: 2
                        fillMode: Image.PreserveAspectFit
                    }

                    Label {
                        id: appTitle
                        color: "#9cafd4"
                        text: qsTr("امیدرزٌاقی")
                        anchors.left: appIcon.right
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.bottom: appIcon.top
                        horizontalAlignment: Text.AlignHCenter
                        anchors.leftMargin: 60
                        anchors.bottomMargin: -36
                        font.bold: false
                        font.pointSize: 10
                        padding: 8
                        font.family: "Tahoma"
                    }

                    MinimizeBtn {
                        id: minimizeBtn
                        x: 458
                        y: 0
                        width: 35
                        anchors.left: appTitle.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        anchors.leftMargin: 0
                        anchors.bottomMargin: 0
                        anchors.topMargin: 0
                    }

                    MaximizeBtn {
                        id: maximizeBtn
                        y: -4
                        width: 35
                        anchors.left: minimizeBtn.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        anchors.topMargin: 0
                        anchors.bottomMargin: 0
                        anchors.leftMargin: 0
                    }

                    CloseBtn {
                        id: closeBtn
                        y: -4
                        width: 35
                        anchors.left: maximizeBtn.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        anchors.bottomMargin: 0
                        anchors.topMargin: 0
                        anchors.leftMargin: 0
                    }
                }

            }



            Rectangle {
                id: content
                color: "#00000000"
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: topBar.bottom
                anchors.bottom: parent.bottom
                anchors.rightMargin: 0
                anchors.leftMargin: 0
                anchors.bottomMargin: 0
                anchors.topMargin: 0








                Rectangle {
                    id: leftMenu
                    x: 0
                    y: -70
                    width: 70
                    color: "#1e222a"
                    anchors.left: parent.left
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom
                    anchors.bottomMargin: 0
                    anchors.topMargin: 0
                    anchors.leftMargin: 0

                    LeftMenuBtn {
                        id: savabeghBtn
                        x: 0
                        y: 0
                        width: 250
                        text: "سوابق مراجعات"
                        isActiveText: true
                        isActiveMenu: true
                        display: AbstractButton.IconOnly
                        //                        x: 0
                        //                        anchors.top: parent.top
                        //                        toggleBtnIcon: "../images/svg/wysiwyg-24px.svg"
                        //                        anchors.topMargin: 0
                    }

                    LeftMenuBtn {
                        id: setAppointmentBtn
                        width: 250
                        text: "نوبت گیری"
                        anchors.left: parent.left
                        anchors.top: savabeghBtn.bottom
                        toggleBtnIcon: "../images/svg/event_note-24px.svg"
                        anchors.leftMargin: 0
                        anchors.topMargin: 0
                        isActiveMenu: true
                        isActiveText: true
                        display: AbstractButton.IconOnly
                    }

                    LeftMenuBtn {
                        id: setAppointmentBtn1
                        width: 250
                        text: "پیام ها"
                        anchors.top: setAppointmentBtn.bottom
                        isActiveMenu: true
                        toggleBtnIcon: "../images/svg/chat-24px.svg"
                        anchors.topMargin: 0
                        isActiveText: true
                        display: AbstractButton.IconOnly
                    }

                }





                Rectangle {
                    id: rectangle
                    color: "#2c313c"
                    anchors.left: leftMenu.right
                    anchors.right: parent.right
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom
                    anchors.leftMargin: 0
                }

                Image {
                    id: bg_content_image
                    y: 0
                    opacity: 0.1
                    anchors.left: leftMenu.right
                    anchors.right: parent.right
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom
                    source: "../images/svg/bg_icon_white.png"
                    anchors.leftMargin: 0
                    fillMode: Image.PreserveAspectFit
                }
            }


        }
    }
}



/*##^##
Designer {
    D{i:0;formeditorZoom:1.33}D{i:17}D{i:18}D{i:19}D{i:20}
}
##^##*/
