import javax.print.attribute.standard.Sides;
import javax.sound.midi.Soundbank;

public class java_linkedlist {

    public static void main(String[] args) {
        NodeList myList = new NodeList();
        myList.addFirst(7);
        myList.addLast(5);
        myList.addFirst(3);
        myList.addLast(1);        
        myList.print();
        myList.bubbleSort();
        myList.print();
        myList.turnover();
        myList.print();
    }

    public static class NodeList {

        private static Node head;

        private class Node{
            private Node next;
            private int value;
        }

        public void addFirst(int value){
            Node node = new Node();
            node.value = value;
            node.next = head;
            head = node;
        }

        public void removeFirst(){
            if (head != null){
                head = head.next;
            }
        }

        public boolean findValue(int val){
            Node pointer = head;
            while (pointer != null){
                if (pointer.value == val)
                    return true;
                pointer = pointer.next;
            }
            return false;
        }

        public void removeLast(){
            Node pointer = head;
            if (pointer == null)
                return;
            if (pointer.next == null) {
                head = null;
                return;
            }
            while (pointer.next.next != null) {
                pointer = pointer.next;
            }
            pointer.next = null;
        }

        public void addLast(int value){
            Node node = new Node();
            node.value = value;
            Node pointer = head;
            if (pointer == null) {
                head = node;
                return;
            }
            while (pointer.next != null) 
                pointer = pointer.next;
            pointer.next = node;       
        }

        public void print(){
            Node pointer = head;
            System.out.print('[');
            while (pointer != null) {
                System.out.print(pointer.value);
                if (pointer.next != null)
                    System.out.print(", ");
                pointer = pointer.next;
            }
            System.out.println(']');
        }

        public void turnover() {
            if (head == null)
                return;
            Node previous = null;
            Node current = head;
            Node next = head.next;
            while(next != null){
                current.next = previous;
                previous = current;
                current = next;
                next = current.next;
            }
            current.next = previous;
            head = current;
        }
        
        public void bubbleSort(){
            if (head == null)
                return;

            Node pointeri = head;
            while (pointeri.next != null){
                Node pointerj = head;
                while(pointerj.next != null){
                    if (pointerj.value > pointerj.next.value) {
                        int temp = pointerj.value;
                        pointerj.value = pointerj.next.value;
                        pointerj.next.value = temp;
                    }
                    pointerj = pointerj.next;
                }
                pointeri = pointeri.next;
            }
        }
    }
}
