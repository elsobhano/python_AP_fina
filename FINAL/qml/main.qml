import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15

import "./controls"
import "controls"
import QtGraphicalEffects 1.15
Window {

    id: window
    width: 1024
    height: 800
    minimumWidth: 640
    minimumHeight: 480
    visible: true
    color: "#1e222a"
    title: qsTr("پورتال")
    flags: Qt.Window | Qt.FramelessWindowHint
    property int windowStatus: 0

    QtObject{
        id:internal
        function minmaxwindow(){
            if(windowStatus == 0){
                window.showMaximized();
                windowStatus =1;
            }else{
                window.showNormal();
                windowStatus =0;
            }
        }
    }

    Rectangle {
        id:bg
        color: "#2c313c"
        border.width: 0
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.rightMargin: 5
        anchors.leftMargin: 5
        anchors.bottomMargin: 5
        anchors.topMargin: 5

        Rectangle {
            id: appContainer
            color: "#00000000"
            border.color: "#00000000"
            border.width: 0
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
                    onClicked: toggleMenuExpanding.running = true
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

                    DragHandler{
                        onActiveChanged: if(active){
                                             window.startSystemMove();
                                         }
                    }

                    Image {
                        id: appIcon
                        width: 28
                        opacity: 1
                        visible: false
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
                        text: "امیدرزاقی"
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
                        onClicked: window.showMinimized()
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
                        onClicked: internal.minmaxwindow()
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
                        onClicked: window.close()
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

                    PropertyAnimation{
                        id:toggleMenuExpanding
                        target: leftMenu
                        property: "width"
                        to:if(leftMenu.width==70)return 250;else{
                               return 70
                           }
                        duration: 500
                        easing.type: Easing.InOutCirc
                    }

                    LeftMenuBtn {
                        id: savabeghBtn
                        x: 0
                        y: 0
                        width: 250
                        text: "سوابق مراجعات"
                        isActiveText: true
                        isActiveMenu: true
                        display: AbstractButton.IconOnly
                        onClicked: {
                            savabeghBtn.isActiveMenu=true
                            setAppointmentBtn.isActiveMenu=false
                            chatBtn.isActiveMenu=false
                            stackView.push(Qt.resolvedUrl("pages/savabeghPage.qml"))
                        }

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
                        isActiveMenu: false
                        isActiveText: true
                        display: AbstractButton.IconOnly
                        onClicked: {
                            savabeghBtn.isActiveMenu=false
                            setAppointmentBtn.isActiveMenu=true
                            chatBtn.isActiveMenu=false
                            stackView.push(Qt.resolvedUrl("pages/setAppointmentPage.qml"))

                        }
                    }

                    LeftMenuBtn {
                        id: chatBtn
                        width: 250
                        text: "پیام ها"
                        anchors.top: setAppointmentBtn.bottom
                        isActiveMenu: false
                        toggleBtnIcon: "../images/svg/chat-24px.svg"
                        anchors.topMargin: 0
                        isActiveText: true
                        display: AbstractButton.IconOnly
                        onClicked: {
                            savabeghBtn.isActiveMenu=false
                            setAppointmentBtn.isActiveMenu=false
                            chatBtn.isActiveMenu=true
                            stackView.push(Qt.resolvedUrl("pages/chatPage.qml"))

                        }
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
                    z: 0
                    anchors.topMargin: 0
                    anchors.leftMargin: 0
                    fillMode: Image.PreserveAspectFit
                }

                StackView {
                    id: stackView
                    anchors.left: leftMenu.right
                    anchors.right: parent.right
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom
                    clip: true
                    anchors.leftMargin: 0
                    initialItem: Qt.resolvedUrl("pages/savabeghPage.qml")
                }


            }


        }

    }

    MouseArea {
        id: leftMouseArea
        anchors.left: parent.left
        anchors.right: bg.left
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.rightMargin: 0
        anchors.leftMargin: 0
        anchors.bottomMargin: 10
        anchors.topMargin: 10
        cursorShape: Qt.SizeHorCursor
        DragHandler{
            target: null
            onActiveChanged: if(active){
                                 window.startSystemResize(Qt.LeftEdge)
                             }
        }
    }

    MouseArea {
        id: topMouseArea
        width: 100
        height: 9
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.topMargin: 0
        anchors.rightMargin: 0
        anchors.leftMargin: 0
        cursorShape: Qt.SizeVerCursor
        DragHandler{
            target: null
            onActiveChanged: if(active){
                                 window.startSystemResize(Qt.TopEdge)
                             }
        }
    }

    MouseArea {
        id: rightMouseArea
        width: 10
        anchors.left: bg.right
        anchors.top: topMouseArea.bottom
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 0
        anchors.topMargin: 0
        anchors.leftMargin: 0
        cursorShape: Qt.SizeHorCursor
        DragHandler{
            target: null
            onActiveChanged: if(active){
                                 window.startSystemResize(Qt.RightEdge)
                             }
        }
    }

    MouseArea {
        id: bottomMouseArea
        y: 471
        height: 9
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.rightMargin: 10
        anchors.leftMargin: 0
        anchors.bottomMargin: 0
        cursorShape: Qt.SizeVerCursor
        DragHandler{
            target: null
            onActiveChanged: if(active){
                                 window.startSystemResize(Qt.BottomEdge)
                             }
        }
    }
    Connections{
        target: backend
        function onSetName(stringText){
                    appTitle.text = stringText;        }

        function onSetPhone(stringText){
            appTitle.text = stringText;
        }
    }

}





/*##^##
Designer {
    D{i:0;height:800;width:1024}
}
##^##*/