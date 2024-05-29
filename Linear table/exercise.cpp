// exercise.cpp

class MyLinkedList {
public:	
	struct LinkedNode {
		int val;
		LinkedNode* next;
		LinkedNode(int val) : val(val), next(nullptr) {}
	};

	MyLinkedList() {
		_size = 0;
		_dummyHead = new LinkedNode(0);
	}

	int get(int index) {
		if(index > _size && index < 0) {
			return -1;
		}
		LinkedNode* cur = _dummyHead;
		while(index--) {
			cur = cur -> next;
		}
		return cur->next->val;
	}

	void addAtHead(int val) {
		LinkedNode* newNode = new LinkedNode(val);
		newNode->next = _dummyHead->next;
		_dummyHead->next = newNode;
		_size++;
	}

	void addAtTail(int val) {
		LinkedNode* newNode = new LinkedNode(val);
		LinkedNode* cur = _dummyHead;
		while(cur->next != nullptr) {
			cur = cur->next;
		}
		cur->next = newNode;
		_size++;
	}

	void addAtIndex(int index, int val) {
		if(index > _size) {
			return;
		}
		LinkedNode* newNode = new LinkedNode(val);
		LinkedNode* cur = _dummyHead;
		while(index--) {
			cur = cur->next;
		}
		newNode->next = cur->next;
		cur->next = newNode;
		_size++;
	}

	void deleteAtIndex(int index) {
		if(index > _size || index < 0) {
			return;
		}
		LinkedNode* cur = _dummyHead;
		while(index--) {
			cur = cur->next;
		}
		LinkedNode* tmp = cur->next;
		cur->next = cur->next->next;
		delete tmp;
		_size--;
	}

	void printLinkedList() {
		LinkedNode* cur = _dummyHead;
		while(cur->next != nullptr) {
			cout << cur->next->val << " ";
			cur = cur->next;
		}
		cout << endl;
	}
private:
	int _size;
	LinkedNode* _dummyHead;
}