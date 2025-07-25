from uuid import uuid4

import course_service_pb2
import course_service_pb2_grpc
import grpc

# Устанавливаем соединение с сервером
channel = grpc.insecure_channel("localhost:50051")
stub = course_service_pb2_grpc.CourseServiceStub(channel)

# Отправляем запрос
response = stub.GetCourse(course_service_pb2.GetCourseRequest(course_id=uuid4().hex))
print(*[response.course_id, response.title, response.description], sep="\n")
