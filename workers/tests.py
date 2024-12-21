from rest_framework import status
from rest_framework.test import APITestCase

from workers.models import Worker


# Create your tests here.


class WorkerTestCase(APITestCase):
    def setUp(self) -> None:
        self.worker1 = Worker.objects.create(
            fio='Worker1',
            team=1,
            salary=10000,
            specialization='Work1'
        )
        self.worker2 = Worker.objects.create(
            fio='Worker2',
            team=2,
            salary=15000,
            specialization='Work2'
        )

    def test_get_team_workers(self):
        response = self.client.get('/api/v1/team/1/WorkerList/')
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            [
                {
                    "id": self.worker1.id,
                    "fio": "Worker1",
                    "team": 1,
                    "salary": 10000,
                    "specialization": "Work1"
                },
            ]
        )

        response = self.client.get('/api/v1/team/2/WorkerList/')
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            [
                {
                    "id": self.worker2.id,
                    "fio": "Worker2",
                    "team": 2,
                    "salary": 15000,
                    "specialization": "Work2"
                },
            ]
        )

        response = self.client.get('/api/v1/team/3/WorkerList/')
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            []
        )

    def test_get_worker(self):
        response = self.client.get(f'/api/v1/worker/{self.worker1.id}/')
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {
                "id": self.worker1.id,
                "fio": "Worker1",
                "team": 1,
                "salary": 10000,
                "specialization": "Work1"
            }
        )

        response = self.client.get(f'/api/v1/worker/{self.worker2.id}/')
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {
                "id": self.worker2.id,
                "fio": "Worker2",
                "team": 2,
                "salary": 15000,
                "specialization": "Work2"
            }
        )

        response = self.client.get(f'/api/v1/worker/1/')
        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

    def test_worker_str(self):
        self.assertEqual(
            self.worker1.__str__(),
            'Worker1'
        )
        self.assertEqual(
            self.worker2.__str__(),
            'Worker2'
        )
