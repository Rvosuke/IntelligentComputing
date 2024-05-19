struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(nullptr) {}
};

ListNode* head = new ListNode(5);

class Solution {
public:
	ListNode* removeElements(ListNode* head, int val) {
		/*这个无虚拟节点的单链表删除元素算法，主要是while的条件判断比较让我疑惑*/
		// Delete head node
		while(head != NULL && head->val == val) {
			ListNode* tmp = head;
			head = head->next;
			delete tmp;
		}

		// Delete not head node
		ListNode* cur = head;
		while(cur != NULL && cur->next != NULL) {
			if (cur->next->val == val) {
				ListNode* tmp = cur->next;
				cur->next = cur->next->next;
				delete tmp;
			} else {
				cur = cur->next;
			}
		}
		return head;
	}

	ListNode* dummyRemoveElement(ListNode* head, int val) {
		ListNode* dummyHead = new ListNode(0);
		dummyHead->next = head;
		ListNode* cur = dummyHead;
		while(cur->next != NULL) {
			if (cur->next == val) {
				ListNode* tmp = cur->next;
				cur->next = cur->next->next;
				delete tmp;
			} else {
				cur = cur->next;
			}
		}
		head = dummyHead->next;
		delete dummyHead;
		return head;
	}

	ListNode* reverseList(ListNode* head) {
		ListNode* tmp;
		ListNode* cur = head;
		ListNode* pre = NULL;
		while(cur) {
			tmp = cur->next;
			cur->next = pre;
			pre = cur
			cur = tmp;
		}
		return pre;
	}

	ListNode* reverse(ListNode* pre, ListNode* cur) {
		if(cur == nullptr) {
			return pre;
		}
		ListNode* tmp = cur->next;
		cur->next = pre;
		return reverse(cur, tmp);
	}

	ListNode* recursiveReverse(ListNode* head) {
		return reverse(nullptr, head)
	}

	ListNode* removeNthFromEnd(ListNode* head, int index) {
		ListNode* dummyHead = new ListNode(0);
		dummyHead->next = head;
		ListNode* fast = dummyHead;
		ListNode* slow = dummyHead;
		while(index-- && fast != nullptr) {
			fast = fast->next;
		}
		while(fast->next != nullptr) {
			fast = fast->next;
			slow = slow->next;
		}
		ListNode* tmp = slow->next;
		slow->next = slow->next->next;
		delete tmp;
		return dummyHead->next;
	}

	ListNode* detectCycle(ListNode* head) {
		ListNode* slow = head;
		ListNode* fast = head;
		while (fast->next != nullptr && fast != nullptr) {
			fast = fast->next->next;
			slow = slow->next;
			if (slow = fast) {
				ListNode* p1 = head;
				ListNode* p2 = fast;
				while (p1 != p2) {
					p1 = p1->next;
					p2 = p2->next;
				}
				return p1;
			}
		}
		return nullptr;
	}
};


class MyLinkedList {
public:

	struct LinkedNode {
		int val;
		LinkedNode* next;
		LinkedNode(int val) : val(val), next(nullptr) {}
	};

	// 初始化链表
	MyLinkedList() {
		_dummyHead = new LinkedNode(0);
		_size = 0;
	}


	// 获取第index个节点的数值，如果index是非法数值则直接返回-1
	// index是从0开始的，第0个节点就是头节点
	int get(int index) {
		if (index > (_size - 1) || index < 0) {
			return -1;
		}
		LinkedNode* cur = _dummyHead->next;
		while(index--) {
			cur = cur->next;
		}
		return cur->val;
	}


	// 在链表最前面插入一个节点，插入完成后，新插入的节点为链表新的头节点
	void addAtHead(int val) {
		LinkedNode* newNode = new LinkedNode(val);
		newNode->next = _dummyHead->next;
		_dummyHead->next = newNode;
		_size++;
	}


	// 在链表最后添加一个节点
	void addAtTail(int val) {
		LinkedNode* newNode = new LinkedNode(val);
		LinkedNode* cur = _dummyHead;
		while(cur->next != nullptr) {
			cur = cur->next;
		}
		cur->next = newNode;
		_size++;
	}


	// 在第index个节点之前插入一个新节点
	// 如果index为0，那么新插入的节点为新的链表的头节点
	// 如果index等于链表的长度，则说明新插入的节点为链表的尾节点
	// 如果index大于链表的长度，则返回空
	void addAtIndex(int index, int val) {
		if(index > _size) {
			return;
		}
		LinkedNode* newNode = new LinkedNode(val);
		while(index--) {
			cur = cur->next;
		}
		newNode->next = cur->next;
		cur->next = newNode;
		_size++;
	}


	// 删除第index个节点，如果index大于或等于链表的长度，则直接返回
	// 注意index是从0开始的
	void deleteAtIndex(int index) {
		LinkedNode* cur = _dummyHead;
		// cur指向待删除节点的前一个节点
		while(index--) {
			cur = cur->next;
		}
		ListNode* tmp = cur->next;
		cur->next = cur->next->next;
		delete tmp;
		_size--;
	}


	// 打印链表
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
};
