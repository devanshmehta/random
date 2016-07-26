struct Node
{
    Node* next;
    int data;
};

//Merges two sorted linked list
Node *mergeList(Node *head1, Node *head2)
{
    Node *dummy;
    dummy->next = 0;
    dummy->data = 0;

    Node *tmp1 = head1;
    Node *tmp2 = head2;
    Node *tmp3 = dummy;
    while (true)
    {
        if (tmp1 == 0)
        {
            tmp3->next = tmp2;
            tmp2 = tmp2->next;
            tmp3 = tmp->next;
            tmp3->next = 0;
            continue;
        }
        if (tmp2 == 0)
        {
            tmp3->next = tmp1;
            tmp1 = tmp1->next;
            tmp3 = tmp->next;
            tmp3->next = 0;
            continue;
        }
        if (tmp1->data <= tmp2->data)
        {
            tmp3->next = tmp1;
            tmp1 = tmp1->next;            
        }
        else
        {
            tmp3->next = tmp2;
            tmp2 = tmp2->next;
        }
        tmp3 = tmp->next;
        tmp3->next = 0;
    }
    return dummy->next;
}

int main()
{
    Node head1;
    head1->next = 0;
    head1-> 
}
